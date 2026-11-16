
import OpenAI from "openai";
import { z } from "zod";
import { zodTextFormat } from "openai/helpers/zod";
import dotenv from "dotenv";

dotenv.config();

const client = new OpenAI({
    apiKey: process.env.OPENAI_API_KEY
});

// 1. Define the output structure using Zod
const Person = z.object({
    name: z.string(),
    age: z.number().int(),
    city: z.string()
});

// 2. Call OpenAI with structured output
const result = await client.responses.parse({
    model: "gpt-4o",
    instructions: "You are a helpful assistant.",
    input: "Give me the name, age and city of a fictional person",

    // Pass the schema
    text: {
        format: zodTextFormat(Person, "person")
    }
});

// 3. Extract parsed output
console.log(result.output_parsed);

// 4. Check the data type
console.log(typeof result.output_parsed);
