import dateparser
from datetime import datetime
from tabulate import tabulate
from rich.console import Console
from rich.table import Table
from rich.text import Text
import arrow
import smtplib
import os, json, schedule, time  # Added back schedule and time
from dotenv import load_dotenv
load_dotenv()

def send_email(subject, body, to_email):
    email_address = os.getenv('EMAIL_ADDRESS')
    email_password = os.getenv('EMAIL_PASSWORD')
    smtp_server = os.getenv('SMTP_SERVER', 'smtp.gmail.com')
    smtp_port = int(os.getenv('SMTP_PORT', 587))
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(email_address, email_password)
    msg = f"Subject: {subject} \n\n {body}"
    server.sendmail(email_address, to_email, msg)
    server.quit()

def notify(reminder):
    subject = f"Reminder: {reminder['Message']}"
    email = reminder["Email"]
    body = f"Priority: {reminder['priority']}\nCategory: {reminder['category']}"
    send_email(subject, body, email)
    print(f"📧 Email sent for reminder {reminder['id']}: {reminder['Message']}")

def execute_reminders():
   folder_name = "Reminder folder"
   file_name = "Reminders list"
   file_path = os.path.join(folder_name, file_name)
   with open(file_path, "r") as file:
    reminders_list = json.load(file)
    for r in reminders_list:
        if r.get("Repeat", False):
            interval = r["Interval"]  # Make sure this matches your data
            unit = r["Unit"]
            
            # Schedule repeating reminders
            if unit == "seconds":
                schedule.every(interval).seconds.do(notify, r)
            elif unit == "minutes":
                schedule.every(interval).minutes.do(notify, r)
            elif unit == "hours":
                schedule.every(interval).hours.do(notify, r)
            elif unit == "days":
                schedule.every(interval).days.do(notify, r)
        else:
            # One-time reminder
            time_obj = datetime.fromisoformat(r["Time"])  # Fixed: removed extra 'datetime'
            def job(rem=r):
                notify(rem)
                return schedule.CancelJob
            schedule.every().day.at(time_obj.strftime("%H:%M")).do(job)
    
    # Keep the program running to execute scheduled tasks
    print("⏰ Reminders are now active. Press Ctrl+C to stop.")
    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n👋 Reminder system stopped.")

# Rest of your code remains the same...
def show_reminders():
    folder_name = "Reminder folder"
    file_name = "Reminders list"
    file_path = os.path.join(folder_name, file_name)
    with open(file_path, "r") as file:
        reminders = json.load(file)
    console = Console()
    table = Table(title="⏰ Reminder List")
    table.add_column("Email", style="blue", no_wrap=False)

    table.add_column("ID", justify="right", style="cyan", no_wrap=True)
    table.add_column("Message", style="magenta")
    table.add_column("Time", style="green")
    table.add_column("Priority", style="bold")
    table.add_column("Category", style="blue")
    table.add_column("Repeat", style="yellow")

    for r in reminders:
        priority = r.get("priority", "").lower()
        if priority == "high":
            priority_text = Text("⚠️ HIGH", style="bold red")
        elif priority == "medium":
            priority_text = Text("⚡ MEDIUM", style="bold yellow")
        else:
            priority_text = Text("✅ LOW", style="bold green")

        category = r.get("category", "")
        category_map = {
            "work": "💼 Work",
            "personal": "👤 Personal",
            "health": "🩺 Health",
            "general": "📌 General"
        }
        category_text = category_map.get(category, category)

        time_value = r.get("Time", "")
        if time_value:
            try:
                time_text = arrow.get(time_value).to('local').humanize()
            except:
                time_text = str(time_value)
        else:
            time_text = "N/A"

        table.add_row(
            r.get("Email", ""),
            str(r.get("id", "")),
            r.get("Message", ""),
            time_text,
            priority_text,
            category_text,
            "🔁 Yes" if r.get("Repeat") else "⏹ No"
        )

    console.print(table)

def add_reminder():
    reminder_list = []
    while True:
        reminder_dict = {}
        message = input("Enter reminder message (or 'done' to finish): ")
        if message.lower() == "done":
            break
        if message:
            reminder_dict["Message"] = message
        else:
            print("Enter reminder message")
            continue
        reminder_dict["id"] = len(reminder_list) + 1
        email = input("Enter your email")
        if email:
            reminder_dict["Email"] = email
        else:
            print("Enter the email you would like to receive reminder")
            continue
        priority = input("Enter priority (high, medium, low): ").lower()
        if priority not in ["high", "medium", "low"]:
            priority = "low"
        reminder_dict["priority"] = priority
        category = input("Enter category (work, personal, health): ").lower()
        if category not in ["work", "personal", "health"]:
            category = "general"
        reminder_dict["category"] = category
        
        time_input = input("Kindly enter how you would want the reminder to execute: ")
        if not time_input:
            continue
        else:
            if "every" not in time_input:
                parse_time = dateparser.parse(time_input)
                if parse_time:
                    print(f"✅ Reminder set for: {parse_time}")
                    reminder_dict["Time"] = parse_time.isoformat()
                    reminder_dict["Repeat"] = False
                    reminder_list.append(reminder_dict)
                else:
                    print("Could not understand that time, kindly enter the right format")
                    continue
            else:
                valid_units = ["seconds", "minutes", "hours", "days"]
                num = time_input.split()
                if len(num) == 3:
                    interval = int(num[1])
                    unit = num[2]
                    if unit not in valid_units:
                        print("❌ Invalid unit, please use seconds/minutes/hours/days")
                        continue
                    else:
                        reminder_dict["Repeat"] = True
                        reminder_dict["Unit"] = unit
                        reminder_dict["Interval"] = interval
                        reminder_list.append(reminder_dict)
                else:
                    unit = num[1]
                    if unit not in valid_units:
                        print("❌ Invalid unit, please use seconds/minutes/hours/days")
                        continue
                    else:
                        reminder_dict["Repeat"] = True
                        reminder_dict["Unit"] = unit
                        reminder_dict["Interval"] = 1
                        reminder_list.append(reminder_dict) 
    print(reminder_list)
    folder_name = "Reminder folder"
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
    file_name = "Reminders list"
    file_path = os.path.join(folder_name, file_name)
    with open(file_path, "w") as file:
        json.dump(reminder_list, file, indent=4)
        print("Reminders saved succesfully")
    
def delete_reminder():
    folder_name = "Reminder folder"
    file_name = "Reminders list"
    file_path = os.path.join(folder_name, file_name)
    
    try:
        with open(file_path, "r") as file:
            reminders = json.load(file)
    except FileNotFoundError:
        print("❌ No reminders file found!")
        return
    except json.JSONDecodeError:
        print("❌ Error reading reminders file!")
        return
        
    if not reminders:
        print("📭 No reminders currently available.")
        return
        
    # Show current reminders first
    print("\n📋 Current reminders:")
    for r in reminders:
        print(f"ID {r['id']}: {r['Message']}")
    
    try:
        reminder_id = int(input("\nEnter reminder ID to delete: "))
    except ValueError:
        print("❌ Please enter a valid number!")
        return
        
    # Check if ID exists
    if not any(r.get("id") == reminder_id for r in reminders):
        print(f"❌ No reminder found with ID {reminder_id}")
        return
        
    # Remove the reminder
    reminders = [x for x in reminders if x.get("id") != reminder_id]
    
    # Reassign IDs
    for idx, r in enumerate(reminders, start=1):
        r["id"] = idx
        
    # SAVE BACK TO FILE (this was missing!)
    with open(file_path, "w") as file:
        json.dump(reminders, file, indent=4)
        
    print("✅ Reminder deleted successfully!")
    
    

  
