# JSON Schema Basics

A JSON Schema defines the expected structure of JSON data.

## Example

```json
{
  "type": "object",
  "properties": {
    "city": {
      "type": "string"
    },
    "temperature": {
      "type": "number"
    }
  },
  "required": [
    "city",
    "temperature"
  ]
}
```

## Why JSON Schema?

- Validates incoming data
- Defines required fields
- Improves API reliability
- Commonly used with LLM function calling
