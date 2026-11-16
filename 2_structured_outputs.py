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
# print(result.output_text)


# naive fix 

result = client.responses.create(
    model="gpt-4o",
    instructions="You are a helpful assistant.Respond in JSON format",
    input="Give me the name, age and city of a fictional person"
)

print(result.output_text)


"""
note : o/p still a sting
```json
{
  "name": "Alex Harper",
  "age": 32,
  "city": "Emerald Bay"
}
```

"""