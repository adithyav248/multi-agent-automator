import os
from dotenv import load_dotenv
from crewai import Crew, Process

from agents import MarketingAgents
from tasks import MarketingTasks

# Load Environment Variables (.env)
load_dotenv()

def run_marketing_automator(topic: str):
    # 1. Initialize Agents
    agents = MarketingAgents()
    researcher = agents.researcher_agent()
    writer = agents.writer_agent()
    editor = agents.editor_agent()

    # 2. Initialize Tasks and assign them to specific agents
    tasks = MarketingTasks()
    research = tasks.research_task(researcher)
    draft = tasks.draft_task(writer)
    edit = tasks.edit_task(editor)

    # 3. Form the Crew
    marketing_crew = Crew(
        agents=[researcher, writer, editor],
        tasks=[research, draft, edit],
        process=Process.sequential, # Tasks will execute one after another
        verbose=True
    )

    # 4. Start the automated process
    print(f"--- Starting Multi-Agent Workflow for Topic: {topic} ---")
    result = marketing_crew.kickoff(inputs={'topic': topic})
    
    # 5. Output the final result
    print("\n\n################################################")
    print("🎯 FINAL POLISHED OUTREACH EMAIL:")
    print("################################################\n")
    print(result)

if __name__ == "__main__":
    # You can change the topic to anything you want to generate leads for
    target_topic = "AI Automation in Healthcare"
    run_marketing_automator(target_topic)