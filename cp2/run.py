import subprocess
from prompt_builder import build_prompt

LLAMA = r"C:\Users\inves\llama.cpp\build\bin\Release\llama-cli.exe"
MODEL = r"C:\dev\Models\Qwen3-4B-UD-Q6_K_XL.gguf"

def run(task: str):
    prompt = build_prompt(task)

    cmd = [
        LLAMA,
        "-m", MODEL,
        "--chat-template", "none",
        "--temp", "0.3",
        "--top-p", "0.9",
        "--repeat-penalty", "1.1",
        "-n", "180",
        "-p", prompt
    ]

    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True
    )

    print(result.stdout)

if __name__ == "__main__":
    run(
        "In 5 bullet points, describe how to design a legal adult social app for consenting adults. "
        "Focus on architecture, onboarding, privacy, consent, safety, and moderation tools."
    )
