from Remind import add_reminder, show_reminders, delete_reminder, execute_reminders
def main():
    while True:
        print("How may we help you")
        print("Add Reminders(1)")
        print("Show Reminders(2)")
        print("Delete Reminders(3)")
        print("Execute Reminders(4")
        option = input("Kindly choose from the option below")
        if option == "1":
            add_reminder()
        elif option == "2":
            show_reminders()
        elif option == "3":
            delete_reminder()
        elif option == "4":
            execute_reminders()
        elif option == "5":
            print("Have a nice day")
            break
        else:
            print("Invalid option kindly choose from the 3 options above")
            
if __name__ == "__main__":
    main()
       