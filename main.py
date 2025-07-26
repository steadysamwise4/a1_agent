import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    # user_input = input("Welcome to A1. What can I help you with today?")
    is_verbose = False
    try:
        args = sys.argv[1:]
        if not args:
            print("No input provided. Exiting program.")
            print("AI Code Assistant")
            print('\nUsage: python main.py "your prompt here"')
            print('Example: python main.py "How do I build a calculator app?"')
            sys.exit(1)
        
        if '--verbose' in args:
            is_verbose = True
        user_inputs = " ".join(args)
        messages = [
            types.Content(role="user", parts=[types.Part(text=user_inputs)]),
            ]
        response = client.models.generate_content(
            model="gemini-2.0-flash-001", 
            contents=messages
            )
    except Exception as e:
        print("No input provided. Exiting program.")
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here"')
        print('Example: python main.py "How do I build a calculator app?"')
        sys.exit(1)
    if is_verbose:
        print(f"User prompt: {user_inputs}")
    print(f"Response: {response.text}")
    if is_verbose:
        ptc = response.usage_metadata.prompt_token_count
        ctc = response.usage_metadata.candidates_token_count
        print(f"Prompt tokens: {ptc}\nResponse tokens: {ctc}")


if __name__ == "__main__":
    main()
