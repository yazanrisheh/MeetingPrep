from crewai import Agent
# from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI

from tools.SearchTool import search_tool
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini",  temperature=0.4,  max_retries=2, max_completion_tokens=10000)
# llm = ChatGroq(model="mixtral-8x7b-32768",  temperature=0.7,  max_retries=3)


# Define the Lead Researcher agent
lead_researcher_agent = Agent(
    role="Lead Researcher",
    goal="Gather and analyze information about {company} and their industry",
    backstory=(
        "As a Research Specialist, your mission is to uncover detailed information "
        "about the individuals and entities participating in the meeting. Your insights "
        "will lay the groundwork for strategic meeting preparation."
    ),
    tools=[search_tool],
    llm=llm,  # Optional
    verbose=True,  # Optional
)

# Define the Product Specialist agent
product_specialist_agent = Agent(
    role="Product Specialist",
    goal="Find key trends, challenges, and opportunities in the industry",
    backstory=(
        "As a Product Specialist, your analysis will identify key trends, "
        "challenges facing the industry, and potential opportunities that "
        "could be leveraged during the meeting for strategic advantage."
    ),
    tools=[search_tool],
    llm=llm,  # Optional
    verbose=True,  # Optional
)

# Define the Sales Strategist agent
sales_strategist_agent = Agent(
    role="Sales Strategist",
    goal="Develop an overall sales approach for {company} and handle potential objections",
    backstory=(
        "As a Strategy Advisor, your expertise will guide the development of "
        "talking points, insightful questions, and strategic angles "
        "to ensure the meeting's objectives are achieved."
    ),
    tools=[search_tool],
    llm=llm,  # Optional
    verbose=True,  # Optional
)

# Define the Briefing Coordinator agent
briefing_coordinator_agent = Agent(
    role="Briefing Coordinator",
    goal="Compile all gathered information into a concise, informative briefing document for the meeting",
    backstory=(
        "You are highly organized and skilled at creating effective meeting structures "
        "that maximize productivity and engagement. Your role is to consolidate the research, "
        "analysis, and strategic insights."
    ),
    tools=[search_tool],
    llm=llm,  # Optional
    verbose=True,  # Optional
)
