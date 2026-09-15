from email.mime import message
from multiprocessing import context
import os
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from openai import OpenAI
from google.adk.agents import LlmAgent
from dotenv import load_dotenv


load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
# DEEP_SEEK_API_KEY = os.getenv("DEEP_SEEK_API_KEY")
# LLM_MODEL = "llama-3.1-8b-instant"
# LLM_MODEL = "openai/gpt-oss-20b" 
LLM_MODEL = os.getenv("LLM_MODEL")
# LLM_MODEL = "groq-math-13b-v1.0"


llm = LlmAgent(
    model = "gemini-2.5-flash",
    name = "cooking_agent",
    description = "A helpful cooking assistant that answers questions about cooking and provides step-by-step solutions. " \
    "And suggest some more nutrient rich recipes based on the ingredients available in the kitchen. "

)

print("GOOGLE_API_KEY exists:", bool(os.getenv("GOOGLE_API_KEY")))
# print(os.getenv("DEEP_SEEK_API_KEY")[:8])
'''
llm = ChatGroq(
    # groq_api_key=DEEP_SEEK_API_KEY,
    groq_api_key = GROQ_API_KEY,
    model= LLM_MODEL,
    temperature=0.7
    
)


llm =  ChatOpenAI(
    openai_api_key = os.getenv("OPENAI_API_KEY"),
    model_name=LLM_MODEL,
    temperature=0.7
)

llm = OpenAI(
    base_url="https://api.deepseek.com",
    api_key=os.getenv("DEEP_SEEK_API_KEY"),
    # model_name=LLM_MODEL
)


prompt = ChatPromptTemplate(
    
    messages=[
        {
            "role": "system",
            "content": "You are a helpful cooking assistant that answers questions about cooking and provides step-by-step solutions."
        },
        {
            "role": "user",
            "content": "{query}"
        }
    ]
)

''''''

print("Chatbot ready! Type 'exit' or 'quit' to stop.\n")

while True:
    query = input("ASK YOUR QUESTION: ")
    if query.lower() in ["exit", "quit"]:
        break

    message = prompt.format_prompt(query=query)
    response = llm.invoke(message)

    # print(response.choices[0].message.content)
    print(response.content)
'''