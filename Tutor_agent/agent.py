from google.adk.agents import Agent
from .sub_agent.math_agent.agent import math_agent
from .sub_agent.physics_agent.agent import physics_agent



Tutor_agent = Agent(
    name="Tutor_agent",
    model="gemini-2.0-flash",
    description=(
        "Agent to answer questions regarding maths and physics related questions"
    ),
    instruction=(
        """You are a helpful agent who can give answers to the math and physics questions.
       Classify the question into math or physics:
          1.`math_agent` use this agent when user asks maths realted questions
          2.`physics_agent` use this agent when user asks physics realted questions
        otherwise give This agent will answer only maths and physics questions.
        if user asks related to both maths and physics call both with related questions.
        """
    ),
    sub_agents=[math_agent, physics_agent]
)