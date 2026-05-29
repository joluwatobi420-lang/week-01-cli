import argparse
import requests

# Create argument parser
parser = argparse.ArgumentParser(description="Git Commit Message Generator CLI")
parser.add_argument("prompt", help="The text or git diff to process")
args = parser.parse_args()

SYSTEM_PROMPT = """You are a git commit message generator. Given a git diff, provide a concise commit message.
Rules:
- First line: <type>(<scope>): <description> in imperative mood, <72 chars.
"""

full_prompt = f"{SYSTEM_PROMPT}\n\nUser Input:\n{args.prompt}"

print("Concerning to Llama 3.2 (1B)... Generataing your commit message...")

try:
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.2:1b", 
            "prompt": full_prompt,
            "stream": False
        },
        timeout=120 
    )
 
    data = response.json()
    print("\n--- Generated Git Commit Message ---")
    print(data.get("response", "No response recieved."))

except requests.exceptions.Timeout:
    print("\n[Error] The request timed out. Try running again.")
except requests.exceptions.ConnectionError:
    print("\n[Error] Could not connect to Ollama. Make sure the Ollama app is open")    

