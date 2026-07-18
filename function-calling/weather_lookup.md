# Weather Function Calling

## Scenario

User:

> What's the weather in Islamabad today?

---

## Tool Selected

```text
weather.get()
```

---

## Arguments

```json
{
  "city": "Islamabad"
}
```

---

## Expected Response

```json
{
  "temperature": 34,
  "condition": "Sunny",
  "humidity": 42
}
```

---

## Why this tool?

The assistant recognizes that the user is requesting real-time weather information and selects the weather tool with the required location parameter.
