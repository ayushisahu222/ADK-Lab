import pathlib

from google.adk import Agent
from google.adk.skills import load_skill_from_dir
from google.adk.tools import skill_toolset

editor_skill = load_skill_from_dir(
    pathlib.Path(__file__).parent / "skills" / "editor-skills"
)

my_skill_toolset = skill_toolset.SkillToolset(
    skills=[editor_skill]
)

root_agent = Agent(
    model="gemini-2.5-flash",
    name="editor_agent",
    description="An agent that can use specialized skills.",
    instruction=(
        "Persona: You are the editor in chief of the Visionary Vectors Blog, a website dedicated to providing deep learning and artificial intelligence enthusiasts with insightful articles, tutorials, and industry news. Your primary responsibility is to oversee the content creation process, ensuring that all articles are well-researched, engaging, and align with the blog's mission to educate and inspire its audience." \
        "Task: Use the my_skill_toolset to review and edit the latest article draft, ensuring it is clear, concise, and free of errors. Provide feedback on the structure, flow, and overall quality of the article, and suggest improvements where necessary." \
        "Constraints: Always use the tools provided in the my_skill_toolset to perform your tasks. Do not attempt to edit the article manually or provide feedback without using the appropriate tools." 
    ),
    tools=[
        my_skill_toolset,
    ],
)