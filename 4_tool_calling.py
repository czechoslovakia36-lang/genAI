from openai import OpenAI
from dotenv import load_dotenv
import json

load_dotenv()

# sdk
client = OpenAI()

# simple api call

result = client.responses.create(
    model="gpt-4o",
    input="What is the weather in Chandigarh?"
)

# print(result.output_text)

# faking api response 1. define the actual python func
def get_weather(city:str):
    return {
        "city": city,
        "temperature":28,
        "unit":"celsius",
        "condition":"sunny"
    }
    
# LLM does understand text - so decribe that to LLM
# describe the func to the model (the tool defination)'

tools = [
     {
         "type":"function",
         "name":"get_weather",
         "description":"Get the current weather for a given city",
         "parameters":{
             "type":"object", 
             "properties":{
                 "city":{
                     "type":"string",
                     "description":"The city to get weather for"
                 }
             }
         },
         "required":["city"]
     }
]

input_messages = [ { "role":"user","content":"What is the current weather in Banglore?"}]

result = client.responses.create(
    model="gpt-4o",
    input=input_messages,
    tools=tools
)

# print(json.dumps(result.to_dict(),indent=2))


# extract the function name and arguments 

tool_call = result.output[0]
function_name = tool_call.name
function_args = json.loads(tool_call.arguments)

# run the function 
function_result = get_weather(function_args["city"])

# print(f" tool called {function_name}")
# print(f"raw result:{function_result}")

# build the full history and everything back

input_messages.append(tool_call)
input_messages.append({
    "type":"function_call_output",
    "call_id":tool_call.call_id,
    "output":json.dumps(function_result)
})

# final results

final_result = client.responses.create(
    model="gpt-4o",
    input=input_messages,
    tools=tools
)


print(final_result.output_text)
