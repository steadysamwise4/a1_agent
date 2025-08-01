import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys
from prompts import system_prompt
from call_function import call_function, available_functions

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    # user_input = input("Welcome to A1. What can I help you with today?")
    is_verbose = "--verbose" in sys.argv

   
    args = []
    for arg in sys.argv[1:]:
        if not arg.startswith("--"):
            args.append(arg)

    if not args:
        print("No input provided. Exiting program.")
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here"')
        print('Example: python main.py "How do I build a calculator app?"')
        sys.exit(1)
        
    user_inputs = " ".join(args)

    if is_verbose:
        print(f"User prompt: {user_inputs}")

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_inputs)]),
        ]
    
    generate_content(client, messages, is_verbose)

def generate_content(client, messages, is_verbose):
    response = client.models.generate_content(
        model="gemini-2.0-flash-001", 
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], 
            system_instruction=system_prompt
        )
    )

    

    if is_verbose:
        ptc = response.usage_metadata.prompt_token_count
        ctc = response.usage_metadata.candidates_token_count
        print(f"Prompt tokens: {ptc}\nResponse tokens: {ctc}")

    if not response.function_calls:
        print("What?")
        print(response.text)
        return

    function_responses = []

    for function_call_part in response.function_calls:
        function_call_result = call_function(function_call_part, is_verbose)
        if (
            not function_call_result.parts
            or not function_call_result.parts[0].function_response
        ):
            raise Exception("empty function call result")
        if is_verbose:
            print(f"-> {function_call_result.parts[0].function_response.response}")
        function_responses.append(function_call_result.parts[0])

    if not function_responses:
        raise Exception("no function responses generated, exiting.")
        


if __name__ == "__main__":
    main()
