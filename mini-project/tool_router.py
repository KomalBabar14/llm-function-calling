"""
Mini Tool Router

A simple simulation of how an LLM might choose a tool
based on a user's request.

Author: Komal Babar
"""

def select_tool(user_input):
    text = user_input.lower()

    if "weather" in text:
        return {
            "tool": "weather.get",
            "arguments": {
                "city": "Islamabad"
            }
        }

    elif "email" in text:
        return {
            "tool": "email.send",
            "arguments": {
                "recipient": "sarah@example.com",
                "subject": "Meeting Reminder",
                "body": "Don't forget tomorrow's meeting."
            }
        }

    elif "meeting" in text or "calendar" in text:
        return {
            "tool": "calendar.create",
            "arguments": {
                "title": "Project Meeting",
                "date": "Tomorrow",
                "time": "3:00 PM"
            }
        }

    else:
        return {
            "tool": None,
            "message": "No suitable tool found."
        }


if __name__ == "__main__":

    examples = [
        "What's the weather in Islamabad?",
        "Send an email to Sarah.",
        "Schedule a meeting tomorrow.",
        "Tell me a joke."
    ]

    for query in examples:
        print("=" * 60)
        print("User:", query)
        print(select_tool(query))
