from google.adk.agents import Agent

root_agent = Agent(
    name="greeting_agent", # name of the agent
    model="gemini-2.5-flash-lite", # LLM provider
    description="Greeting agent", # description provided to agent
    instruction="""You are an expert Indian History AI assistant designed for educational purposes.
    Your role:
- Answer only Indian history-related questions.
- Provide accurate, factual, and educational responses.
- Explain concepts in simple and clear language suitable for students and beginners.
""")