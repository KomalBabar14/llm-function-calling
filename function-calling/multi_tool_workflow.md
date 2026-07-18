# Multi-Tool Workflow

## Scenario

User:

> Schedule a meeting with Ali tomorrow at 3 PM and email him the invitation.

---

## Step 1: Find the Contact

### Tool

```text
contacts.search()
```

### Arguments

```json
{
  "name": "Ali"
}
```

---

## Step 2: Create the Calendar Event

### Tool

```text
calendar.create()
```

### Arguments

```json
{
  "title": "Meeting with Ali",
  "date": "Tomorrow",
  "time": "3:00 PM"
}
```

---

## Step 3: Send the Email

### Tool

```text
email.send()
```

### Arguments

```json
{
  "recipient": "ali@example.com",
  "subject": "Meeting Invitation",
  "body": "Hi Ali, our meeting has been scheduled for tomorrow at 3:00 PM."
}
```

---

# Reasoning

The assistant performs the tasks in this order:

1. Find Ali's contact information.
2. Create the calendar event.
3. Send the invitation email.

If Ali's contact information is not found, the assistant should ask the user for an email address instead of guessing.
