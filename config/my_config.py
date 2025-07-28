import os
from openai import Runcongfig
from agents import AsyncOpenAI, openaiChatCompletion


gemini_api_key ="GEMINI_API_KEY",
gemini_api_url = "https://api.gemini.google.com/v1beta2"


Client=AsyncOpenAI({
    "gemini_api_key": os.getenv("GEMINI_API_KEY", "default_api_key"),
    "gemini_api_url": os.getenv("GEMINI_API_URL", "https://api.gemini.google.com/v1beta2"),
    "gemini_model": os.getenv("GEMINI_MODEL", "gemini-1.5-flash"),
    
})

model=openaiChatCompletion({
    "gemini_model": os.getenv("GEMINI_MODEL", "gemini-1.5-flash"),
    
})

run_config = Runcongfig(
    client=Client,
    model=model,
    tracing_disabled=True
    
)