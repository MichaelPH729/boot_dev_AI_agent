import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
prompt ="".join(sys.argv[1:])

def main():
    if not prompt:
        print("AI Assistant requires a string input, EX: python main.py 'What are the most important words a man can say?'")
        sys.exit(1)

    messages = [types.Content(role="user", parts=[types.Part(text=prompt)])]
    response = client.models.generate_content(model='gemini-2.0-flash-001', contents=messages)
    print(response.text)
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()
