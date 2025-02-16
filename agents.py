import os
from crewai import Agent
from tools import tool
from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
os.environ["GEMINI_API_KEY"] = os.getenv("GEMINI_API_KEY")

llm = "gemini/gemini-1.5-flash"


#creating Agent
news_researcher=Agent(
    role="senior researcher",
    goal="Uncover groundbreaking technolgies in {topic}",
    verbose=True,
    memory=True,
    backstory=(
        """Driven by curiosity, you're at the forefront of
        innovation, eager to explore and share knowledge that could change
        the world."""
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=True

)

#creating writter Agent
news_writer = Agent(
  role='Writer',
  goal='Narrate compelling tech stories about {topic}',
  verbose=True,
  memory=True,
  backstory=(
    """With a flair for simplifying complex topics, you craft
    engaging narratives that captivate and educate, bringing new
    discoveries to light in an accessible manner."""
  ),
  tools=[tool],
  llm=llm,
  allow_delegation=False
)

