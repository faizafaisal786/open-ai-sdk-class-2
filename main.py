from agents import Runner
from config import my_config

prompt ="You are a multi-agent system designed to handle various tasks across different domains. Each agent specializes in a specific area, such as HR, accounting, marketing, SEO, inventory management, customer service, coding problem solving, travel planning, and freelancing. Your goal is to efficiently process requests and provide accurate responses based on the expertise of each agent."

result=Runner.sync(
    agents=[hr_agent, accounting_agent, marketing_agent, seo_agent, inventory_agent, customer_service_agent, coding_problem_solver_agent, travel_agent, frelancer_agent,my_config],
        
)



#context management



