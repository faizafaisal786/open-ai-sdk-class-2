from agents import Agent
from config.my_config import model

next_js_assistant=Agent(
    name="next_js_assistant",
    instructions="You are a Next.js assistant. You are responsible for helping the user with their Next.js project. You will be given a list of tasks and you will need to complete them. You will also need to communicate with the user and provide feedback on the progress of the project.",
    model=model,
)

python_assistant=Agent(
    name="python_assistant",
    instructions="You are a Python assistant. You are responsible for helping the user with their Python project. You will be given a list of tasks and you will need to complete them. You will also need to communicate with the user and provide feedback on the progress of the project.",
    model=model,
)

triage_agent=Agent(
    name="triage_agent",
    instructions="You are a triage agent. You are responsible for helping the user with their project. You will be given a list of tasks and you will need to complete them. You will also need to communicate with the user and provide feedback on the progress of the project.",
    model=model,
    handoffs=[next_js_assistant,python_assistant],
    
)



