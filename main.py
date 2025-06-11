import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

user_prompt = " ".join(sys.argv[1:])

# sys.argv[0] => 파일 이름
messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)])
]

# print(messages)
# print(",".join(sys.argv[1:]))

try:
    if messages:
        response = client.models.generate_content(
            model="gemini-2.0-flash-001",
            contents=messages,
        )
        if "--verbose" in user_prompt:
            print(f"User prompt: {user_prompt}")
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
            print(f"Response: {response.text}")
        else:
            print(f"{response.text}")
except:
    print("There is no prompt input")
    sys.exit(1)



