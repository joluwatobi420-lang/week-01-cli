import requests

url = "http://localhost:11434/api/generate"

payload = {
    "model": "llama3.2:1b",
    "prompt": "Explain async/await in one paragraph.",
    "stream": False
}

response = requests.post(url, json=payload)

data = response.json()

print(data["response"])
python hello.py


