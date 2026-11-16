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


# print(result.output_text)


# system prompt , temp, max_tokens


result = client.responses.create(
    model='gpt-4o',
    instructions="you are a helpful assistant who makes jokes.",
    input="What is square root of 49?",
    temperature=0.7,
    max_output_tokens=100
)

print(result.output_text)

# token usages

# print(f"input token: {result.usage.input_tokens}")
# print(f"o/p token: {result.usage.output_tokens}")
# print(f"total token: {result.usage.total_tokens}"
      
#       )


# streaming 

stream = client.responses.create(
    model='gpt-4o',
    instructions="you are a helpful assistant.",
    input="tell me short story about a robot",
    # temperature=0.7,
    # max_output_tokens=100
    stream=True
)


for event in stream:
    if hasattr(event,'delta'):
        print(event.delta,end="",flush=True)
                                        
                                        
# js equivalent 

# for await (const event of stream) {
#     if (event.type === "response.output_text.delta") {
#         process.stdout.write(event.delta);
#     }
# }