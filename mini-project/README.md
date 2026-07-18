# Mini Tool Router

This project demonstrates a simplified version of tool selection used in Large Language Models (LLMs).

## Workflow

1. Read the user's request.
2. Identify the user's intent.
3. Select the appropriate tool.
4. Extract the required arguments.
5. Return the selected tool and arguments.

## Example

### User

```
What's the weather in Islamabad?
```

### Selected Tool

```
weather.get
```

### Arguments

```json
{
  "city": "Islamabad"
}
```

---

This is a simplified educational example and does not call real APIs.
