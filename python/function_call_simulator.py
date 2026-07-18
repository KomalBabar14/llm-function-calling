def send_email(recipient, subject, body):
    print("Calling email.send()")
    print(f"To: {recipient}")
    print(f"Subject: {subject}")
    print(f"Body: {body}")

send_email(
    "sarah@example.com",
    "Meeting Reminder",
    "Don't forget our meeting tomorrow at 10:00 AM."
)
