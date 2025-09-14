

Smart Reminder System

The Smart Reminder System is a powerful, feature-rich command-line reminder application designed to send email notifications. It supports both one-time and recurring reminders, offering a flexible and user-friendly experience.

Features

Email Notifications: Receive reminders directly in your inbox.

Flexible Scheduling: Set up one-time reminders or recurring intervals.

Priority Levels: Organize tasks by urgency—High, Medium, or Low.

Categories: Classify reminders under Work, Personal, Health, or General.

Natural Language: Input time in human-friendly formats like "tomorrow at 3pm" or "every 2 hours."

Beautiful Display: Enjoy a rich, colorful terminal interface.

Persistent Storage: Reminders are saved locally in a JSON file.

Real-time Execution: Continuously monitors and sends scheduled reminders.


Quick Start

Prerequisites

Before running the application, install the necessary Python packages using:

pip install dateparser tabulate rich arrow schedule python-dotenv

Installation

1. Clone or download the repository to your computer.


2. Install the required dependencies using the command above.


3. Set up your email credentials by creating a .env file (see the Security Setup section below).


4. Run the application with:



python main.py

Usage

Adding Reminders

When adding a reminder, you'll be prompted for the following information:

Reminder Message: What you want to be reminded about (e.g., "Take medicine").

Email Address: Where you want to receive the reminder.

Priority Level: Choose from High, Medium, or Low.

Category: Select from Work, Personal, Health, or General.

Time: When you want to be reminded (supports natural language).


Scheduling Options

The application allows flexible time input:

One-time reminders: Enter times like "tomorrow at 3pm", "January 15 at 9am", "in 2 hours", or "next Monday at 10am."

Recurring reminders: Set up repeating reminders such as "every 2 hours", "every 30 minutes", "every day", or "every week."


Priority Levels

High Priority: Critical reminders requiring immediate attention (displayed in red).

Medium Priority: Important reminders to be addressed soon (displayed in yellow).

Low Priority: General reminders for less urgent tasks (displayed in green).


Categories

Work: Professional tasks such as meetings, deadlines, and work assignments.

Personal: Personal tasks like calling family, paying bills, or appointments.

Health: Medical reminders such as taking medication, doctor visits, or health check-ups.

General: Other reminders that don’t fall into the above categories.


Security Setup

For security reasons, never hard-code your email credentials directly in the code. Instead, create a .env file in your project directory with the following content:

EMAIL_ADDRESS=your-email@gmail.com
EMAIL_PASSWORD=your-gmail-app-password
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587

Important Security Note: Use a Gmail App Password instead of your regular Gmail password. Enable two-factor authentication on your Google account, and then generate a specific app password for this project.

Never commit your .env file to GitHub or share it publicly, as it contains sensitive information.

How It Works

Main Menu

Upon launching the application, you’ll see a clean and intuitive menu offering several options:

Add new reminders.

View your current reminders in a color-coded table.

Delete outdated reminders.

Execute the reminder system to monitor and send notifications.


Reminder List Display

The reminders are displayed in a visually appealing table with the following details:

Email Address: Where notifications will be sent.

Unique ID: Each reminder has a unique identifier.

Reminder Message: A brief description of the reminder.

Time: When the reminder will trigger (shown in a human-readable format).

Priority Level: Color-coded for easy identification.

Category: Clearly marked with appropriate icons.

Repeat Status: Whether the reminder is one-time or recurring.


Technical Features

Natural Language Processing: Utilizes the dateparser library to interpret time expressions like "tomorrow at 3pm" or "in 2 hours."

Email Integration: Connects to Gmail's SMTP server for professional email notifications.

Scheduling Engine: Efficiently handles both one-time and recurring reminders via the schedule library.

Rich Terminal Interface: Uses the rich library for a visually rich and colorful terminal experience.

JSON Data Persistence: Saves reminder data locally, ensuring it persists across application restarts.

Error Handling: Comprehensive error checking with user-friendly messages.

Input Validation: Ensures reminders are correctly created with proper input formats.


Project Structure

Remind.py: Core reminder logic, including email sending, reminder execution, and data management.

main.py: Provides the command-line interface for user interactions.

Reminder folder: Stores reminder data in JSON format.

.env: Contains email credentials (not included in the repository for security reasons).

README.md: Documentation for the project.


Future Enhancements

Graphical User Interface (GUI): Develop a web-based or desktop GUI for easier user interaction.

Multiple Email Providers: Support additional email services beyond Gmail.

SMS Notifications: Integrate SMS text message notifications.

Calendar Integration: Sync with Google Calendar, Outlook, or other calendar platforms.

Cloud Synchronization: Store reminders in the cloud for access across multiple devices.

Mobile Application: Create a smartphone app version.

Team Reminders: Allow users to share reminders with family members or work teams.


Contributing

If you’d like to contribute:

1. Fork the repository on GitHub.


2. Create a feature branch for your changes.


3. Implement your improvements with clear, descriptive commit messages.


4. Thoroughly test your changes.


5. Push your changes to your forked repository.


6. Open a Pull Request with a detailed description of your improvements.



License

This project is licensed under the MIT License. You are free to use, modify, and distribute the code as long as you include the original copyright notice.



Author
[Dev-Paul-01] - Full Stack Developer
GitHub: @Dev-Paul-01
Email: oluwaseyiogunsola90@gmail.com

If you find this project helpful, please consider giving it a star on GitHub! Your support helps others discover useful tools like this one.




