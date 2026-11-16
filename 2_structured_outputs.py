from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# sdk
client = OpenAI()

# STRUCTURED O/P

result = client.responses.create(
    model="gpt-4o",
    instructions="You are a helpful assistant",
    input="Give me the name, age and city of a fictional person"
)
# note: type of output is string
print(result.output_text)


# naive fix 
