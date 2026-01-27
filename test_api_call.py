# Importing the os module
# This module is for interacting with the OS
import os

# Importing load_dotenv function from dotenv module
# This function loads env variables from a .env file
from dotenv import load_dotenv # type: ignore

# Using the function
load_dotenv()

# Getting and printing API key
# This uses the os module to get the API key
api_key = os.getenv("GEMINI_API_KEY")

# Importing the genai module
from google import genai
from google.genai import types # type: ignore
# Initializing the genai client
client = genai.Client()

# Defining System Instruction
instruction='''You are an Expert that Specializes in Computer Science,
        You are great and helpful at answering questions related to programming and computer science.
        Provide detailed and informative responses to user queries.
        Do not answer any question outside the context of Computer Science.
        Avoid romantic, NSFW, or violent content.
        '''
# Making an API call to generate content
response = client.models.generate_content (
    model="gemini-3-flash-preview", #Indicating model to use
    # Adding System Instruction
    config=types.GenerateContentConfig(
        system_instruction=instruction
    ),
    #Adding User Prompt
    contents= input("Input your prompt: ")
)

# Printing the response
print(response.text)