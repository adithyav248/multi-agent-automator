import os
from crewai import Agent
from crewai_tools import SerperDevTool
from langchain_google_genai import ChatGoogleGenerativeAI

class MarketingAgents:
    def __init__(self):
        # The SerperDevTool allows the agent to search the internet
        self.search_tool = SerperDevTool()

        # Initialize the Google Gemini LLM
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash", # You can also use "gemini-1.5-pro" for deeper reasoning
            verbose=True,
            temperature=0.7,
            google_api_key=os.environ.get("GEMINI_API_KEY")
        )

    def researcher_agent(self):
        return Agent(
            role='Senior Market Researcher',
            goal='Discover the latest trends, pain points, and news regarding {topic}',
            backstory=(
                "You are an elite market researcher working for a top-tier digital marketing agency. "
                "You excel at scraping the web, analyzing current market conditions, and finding "
                "actionable data that can be used to generate highly targeted leads."
            ),
            verbose=True,
            allow_delegation=False,
            tools=[self.search_tool],
            llm=self.llm  # Injecting Gemini here
        )

    def writer_agent(self):
        return Agent(
            role='Expert Marketing Copywriter',
            goal='Draft a highly engaging, hyper-personalized cold outreach email based on market research',
            backstory=(
                "You are a world-class copywriter known for achieving sky-high open and reply rates. "
                "You take raw research data and weave it into compelling, empathetic, and persuasive "
                "narratives that speak directly to the target lead's pain points."
            ),
            verbose=True,
            allow_delegation=False,
            llm=self.llm  # Injecting Gemini here
        )

    def editor_agent(self):
        return Agent(
            role='Chief Content Editor',
            goal='Critique, refine, and polish marketing content to ensure maximum conversion',
            backstory=(
                "You are a meticulous editor with a strict eye for detail. You review drafts to ensure "
                "they are grammatically flawless, lack marketing fluff, and have a powerful, clear "
                "Call-to-Action (CTA). You do not settle for mediocre copy."
            ),
            verbose=True,
            allow_delegation=False,
            llm=self.llm  # Injecting Gemini here
        )