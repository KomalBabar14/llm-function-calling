# Prompt Engineering Patterns

## Zero-Shot Prompting

The model is asked to perform a task without any examples.

### Example

**Prompt**

```
Translate the following sentence into French:

Hello, how are you?
```

---

## One-Shot Prompting

The model is given one example before solving the task.

### Example

Input:
Apple → Fruit

Now classify:

Carrot →

Output:
Vegetable

---

## Few-Shot Prompting

The model is given multiple examples.

### Example

Input:
Apple → Fruit
Carrot → Vegetable
Rose → Flower

Now classify:

Mango →

Output:
Fruit

---

## Chain-of-Thought Prompting

The model is encouraged to reason step by step before giving an answer.

This technique is useful for mathematical reasoning, planning, and complex decision-making.
