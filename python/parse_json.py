import json

data = {
    "name": "Komal",
    "role": "LLM Trainer",
    "skills": ["Python", "JSON", "REST APIs"]
}

print(json.dumps(data, indent=4))
