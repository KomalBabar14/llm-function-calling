# Function Calling Best Practices

## Before Calling a Tool

- Understand the user's intent.
- Select the correct tool.
- Extract all required arguments.
- Validate the provided information.

## If Information Is Missing

Ask a clarification question instead of guessing.

Example:

User:
> Send an email to John.

Assistant:

> Which John would you like me to email?

## Multiple Tools

If multiple tools are required, execute them in a logical order.

Example:

1. Search contact
2. Create calendar event
3. Send email
