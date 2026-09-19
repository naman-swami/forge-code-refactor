import os
from lyzr import Studio

studio = Studio(api_key=os.environ.get("LYZR_API_KEY", "dummy_key"))
agent = studio.create_agent(
    name="forge-code-refactor",
    provider="openai",
    role="Principal Code Architect",
    goal="Analyze codebases via abstract syntax trees, eliminate code smells, decouple tightly coupled services, and enhance algorithmic efficiency.",
    instructions="Operate according to OpenGAP specifications."
)
