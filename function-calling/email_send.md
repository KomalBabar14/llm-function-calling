# Email Function Calling

## Scenario

A user asks:

> Send an email to Sarah reminding her about tomorrow's meeting at 10 AM.

---

## Tool Selected

```text
email.send()
```

---

## Arguments

```json
{
  "recipient": "Sarah",
  "subject": "Meeting Reminder",
  "body": "Hi Sarah, this is a reminder that our meeting is scheduled for tomorrow at 10:00 AM."
}
```

---

## Why this tool?

The user's intent is to send an email.

The assistant should:

- Identify the intent.
- Select the appropriate tool.
- Extract the required arguments.
- Call the tool.

---

## Interview Tip

Before calling the tool, the assistant should verify that all required information is available.

If information is missing (for example, no recipient is provided), the assistant should ask a clarification question instead of guessing.
