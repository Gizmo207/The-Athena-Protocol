def build_prompt(user_input: str) -> str:
    with open("persona_athena.txt", "r", encoding="utf-8") as f:
        persona = f.read().strip()

    with open("task_designer.txt", "r", encoding="utf-8") as f:
        task = f.read().strip()

    with open("guardrails.txt", "r", encoding="utf-8") as f:
        guardrails = f.read().strip()

    prompt = f"""{persona}

{task}

{guardrails}

TASK:
{user_input}

RESPONSE:
"""
    return prompt
