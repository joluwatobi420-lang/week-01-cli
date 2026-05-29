import argparse
import sys 
import os
import requests
    
parser = argparse.ArgumentParser()    
parser.add_argument('--file', type=str)
parser.add_argument('text', type=str, nargs='*')  
parser.add_argument('--model', type=str, default='llama3.2:1b')
parser.add_argument('--temperature', type=float, default=0.3)
parser.add_argument('--json', action='store_true')
parser.add_argument('--verbose', action='store_true')

args = parser.parse_args()

input_data = ""
if not sys.stdin.isatty():
        input_data = sys.stdin.read()
elif args.text and os.path.path.exists(args.file):
        input_data = f.read()
elif args.text:
        input_data = " ".join(args.text)       

url = "http://localhost:11434/api/generate"
payload = {
    "model": args.model,
    "prompt": input_data.strip(),
    "stream": False,
    "options": {"temperature": args.temperature}
}

if args.json:
    payload["format"] = "json"

try:
    response = requests.post(url, json=payload, timeout=120)
    print(response.json().get("response", ""))
except Exception as e:
    print(f"Connection Error: Make sure Ollama is open! Details: {e}")


   


                 