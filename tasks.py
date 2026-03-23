from crewai import Task

class MarketingTasks:
    def research_task(self, agent):
        return Task(
            description=(
                "Investigate the internet for the latest trends, news, and pain points related to '{topic}'. "
                "Identify specific buzzwords, recent industry shifts, and opportunities that a B2B SaaS "
                "company could leverage to pitch their services to leads."
            ),
            expected_output=(
                "A detailed 3-part research report containing: "
                "1. Top 3 current trends in the space. "
                "2. The biggest pain points the target audience is facing right now. "
                "3. A list of relevant buzzwords to use in marketing copy."
            ),
            agent=agent
        )

    def draft_task(self, agent):
        return Task(
            description=(
                "Using the research report provided by the Senior Market Researcher, write a concise, "
                "3-paragraph cold outreach email targeting potential leads in the '{topic}' industry. "
                "Ensure the tone is professional yet conversational. Include a compelling subject line "
                "and a clear Call-to-Action (CTA) at the end."
            ),
            expected_output=(
                "A draft of a personalized cold outreach email containing a Subject Line, "
                "Body (max 3 paragraphs), and a CTA."
            ),
            agent=agent
        )

    def edit_task(self, agent):
        return Task(
            description=(
                "Review the drafted cold outreach email. Critique it for clarity, persuasiveness, "
                "and brevity. Ensure it addresses the pain points identified in the research. "
                "Make necessary edits to improve the flow and maximize the potential response rate."
            ),
            expected_output=(
                "The final, polished version of the cold outreach email ready to be sent to a lead, "
                "along with a brief 2-sentence explanation of the edits made."
            ),
            agent=agent
        )