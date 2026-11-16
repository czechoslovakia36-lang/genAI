from openai import OpenAI
from dotenv import load_dotenv
from pydantic import BaseModel

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

# print(result.output_text)


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

# USE pydantic?
# what is pydantic - lets u define the output structure/shape of the data
# when u pass text_format=Person, the sdk converts this class into a json schema and sends
# it to openAIs server. the model is contrained at the server lvel
# to only return data that matches this schema 


class Person(BaseModel):
    name :str
    age : int
    city: str


result = client.responses.parse(
    model="gpt-4o",
    instructions="You are a helpful assistant.Respond in JSON format",
    input="Give me the name, age and city of a fictional person",
    text_format=Person
)


print(result.output_parsed)
print(type(result.output_parsed))