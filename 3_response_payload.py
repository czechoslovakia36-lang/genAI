from openai import OpenAI
from dotenv import load_dotenv
import json

load_dotenv()

# sdk
client = OpenAI()

# simple api call

result = client.responses.create(
    model="gpt-4o",
    input="What is the square root of 49"
)

print(json.dumps(result.to_dict(),indent=2))