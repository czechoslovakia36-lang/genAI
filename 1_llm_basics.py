from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# sdk
client = OpenAI()

# simple api call

result = client.responses.create(
    model="gpt-4o",
    input="What is the square root of 49"
)



# extract o/p response
# print(result.output_text)

# multi turn conversion 
result = client.responses.create(
    model="gpt-4o",
    instructions="You are a helpful assistant",
    input=[
        {"role": "user", "content":"my name is Harish"} , 
        {"role": "assistant", "content":"nice to meet you Harish"} , 
        {"role": "user", "content":"what is my name?"} , 
        ]
)


print(result.output_text)

# token usages

print(f"input token: {result.usage.input_tokens}")
print(f"o/p token: {result.usage.output_tokens}")
print(f"total token: {result.usage.total_tokens}"
      
      )


