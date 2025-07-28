from agents import Agent, ModelSettings
from config import my_config
from agents.agent import StopAtTools
from my_tools.my_tools import hr_agent,accounting_agent

Hr_agent=Agent(
    name="hr_agent",
    instructions="you are a human resources agent.You are responsible for hiring and managing employees. You will be given a list of condidates and their qualifications. you will also be given a list of taskes  that need to be completed. you will need to assign tasks to condidates based on their qualifications and experience." \
    "You will also need to manage the employees and ensure that they are completing their tasks on time. You will need to communicate with the employees and provide feedback on their performance.",
    tools=[hr_agent,accounting_agent]
    model_settings=ModelSettings(tool_choice="required")
)


accoutenting_agent=Agent(
    name="accounting_agent",
    instructions="you are an accounting agent. You are responsible for managing the financial records of the company. You will be given a list of transactions and you will need to categorize them and ensure that they are recorded correctly. You will also need to prepare financial reports and provide insights on the company's financial performance.",
    )

marketing_agent=Agent(
    name="marketing_agent",
    instructions="you are a marketing agent. You are responsible for promoting the company's products and services. You will be given a list of marketing campaigns and you will need to create and execute them. You will also need to analyze the results of the campaigns and provide insights on how to improve them.",
    tools=[]
)

seo-agent=Agent(
    name="seo_agent",
    instructions="you are a search engine optimization agent. You are responsible for improving the company's online presence and visibility. You will be given a list of keywords and you will need to optimize the company's website and content for those keywords. You will also need to analyze the results and provide insights on how to improve the company's online presence.",
    tools=[]
)

inventory_agent=Agent(
    name="inventory_agent",
    instructions="you are an inventory management agent. You are responsible for managing the company's inventory. You will be given a list of products and their quantities. You will need to ensure that the inventory is accurate and up-to-date. You will also need to analyze the inventory data and provide insights on how to improve the inventory management process.",
    tools=[]
)


customer_service_agent=Agent(
    name="customer_service_agent",
    instructions="you are a customer service agent. You are responsible for handling customer inquiries and complaints. You will be given a list of customer inquiries and you will need to respond to them in a timely and professional manner. You will also need to analyze the customer feedback and provide insights on how to improve the customer service process.",
    tools=[]
)

coding_problem_solver_agent=Agent(
    name="coding_problem_solver_agent",
    instructions="you are a coding problem solver agent. You are responsible for solving coding problems and providing solutions. You will be given a list of coding problems and you will need to analyze them and provide solutions. You will also need to explain the solutions in a clear and concise manner.",
    tools=[openaiChatCompletion]

)

travel_agent=Agent(
    name="travel_agent",
    instructions="you are a travel agent. You are responsible for planning and organizing travel arrangements for clients. You will be given a list of travel requests and you will need to find the best options for flights, accommodations, and activities. You will also need to provide recommendations and insights on travel destinations.",
    tools=[]
)

frelancer_agent=Agent(
    name="freelancer_agent",
    instructions="you are a freelancer agent. You are responsible for managing freelance projects and tasks. You will be given a list of freelance projects and you will need to assign tasks to freelancers based on their skills and availability. You will also need to communicate with freelancers and provide feedback on their work.",
    tools=[]

)
agent=Agent(name="sub ka manager",
instructions=a"p sub tools k manager hu"
model=model,
tools=[coding_problem_solver_agent.as_tool(tool_name="coding_problem_solver",tool_description="you are the coding problem solver.")]


)