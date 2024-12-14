# from crewai_tools import  SerperDevTool
from crewai.tools import tool
from tavily import TavilyClient
from dotenv import load_dotenv

load_dotenv()
tavily_client = TavilyClient()

@tool("Tavily Search Tool")
def search_tool(query: str):
    """A powerful tool for conducting detailed online research about companies, their industry position, key trends, and relevant insights. Ideal for gathering information to support meeting preparation and strategic decision-making"""
    return tavily_client.search(query, search_depth="advanced", max_results=1, include_raw_content=True)
