# Calendar Function Calling

## Scenario

User:

> Schedule a project review meeting next Monday at 2 PM.

---

## Tool Selected

```text
calendar.create()
```

---

## Arguments

```json
{
  "title": "Project Review Meeting",
  "date": "Next Monday",
  "time": "2:00 PM"
}
```

---

## Why this tool?

The assistant recognizes that the user wants to create a calendar event and extracts the required scheduling information before calling the tool.

---

## Best Practice

If the user does not specify a date or time, the assistant should ask for the missing information before creating the event.
