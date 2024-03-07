<p align="center">
   <img src="https://github.com/harehimself/hare_crewai-lab/blob/9dc02d7079cf74ddafccb3ebf195c2393c3ebefa/Hare_Network-Analytics.png" alt="Hare Crew AI Lab">
</p>

<p align="center">
   Experimentation with CrewAI, a framework designed for orchestrating a cohort of autonomous AI agents. By utilizing a "crew" of specialist agents, CrewAI empowers agents to collaborate on complex tasks. Many see this approach as the beginnings of "intelligent agent swarms."
</p>
<br>

<p align="center">
  <a href="https://github.com/harehimself/hare_crewai/graphs/contributors">
    <img src="https://img.shields.io/github/contributors/harehimself/hare_crewai" alt="Contributors"></a>
  <a href="https://github.com/harehimself/hare_crewai/network/members">
    <img src="https://img.shields.io/github/forks/harehimself/hare_crewai" alt="Forks"></a>
  <a href="https://github.com/harehimself/hare_crewai/stargazers">
    <img src="https://img.shields.io/github/stars/harehimself/hare_crewai" alt="Stars"></a>
  <a href="https://github.com/harehimself/hare_crewai/issues">
    <img src="https://img.shields.io/github/issues/harehimself/hare_crewai" alt="Issues"></a>
  <a href="https://github.com/harehimself/hare_crewai/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/harehimself/hare_crewai" alt="MIT License"></a>
</p>

<br><br>

## Table of Contents
  - [Features](#features)
  - [Getting Started](#getting-started)
  - [License](#license)


<br>

## Features
**Role-Based Agent Design:** $\color{gray}{\textsf{Customize agents with specific roles, goals, and tools.}}$<br>
**Autonomous Inter-Agent Delegation:** $\color{gray}{\textsf{Agents can autonomously delegate tasks and inquire amongst themselves.}}$<br>
**Flexible Task Management:** $\color{gray}{\textsf{Define tasks with customizable tools and assign them to agents dynamically.}}$<br>
**Process-Driven:** $\color{gray}{\textsf{Sequential task execution and hierarchical processes.}}$<br>
**Save Output as File:** $\color{gray}{\textsf{Save the output of individual tasks as a file, so you can use it later.}}$<br>
**Parse Output as Pydantic or JSON:** $\color{gray}{\textsf{Parse the output of individual tasks as a Pydantic model or as JSON.}}$<br>
**Compatible With Open-Source Models:** $\color{gray}{\textsf{Run your crew using Open AI or open source / local models.}}$<br>

<br>

## Getting Started
To get started with CrewAI, follow these simple steps:<br><br>

### 1. Installation
```python
pip install crewai
```
If you want to also install crewai-tools, which is a package with tools that can be used by the agents, but more dependencies, you can install it with, example bellow uses it:

```python
pip install 'crewai[tools]'
```
<br>

### 2. Setting Up Your Crew

```python
import os
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool

os.environ["OPENAI_API_KEY"] = "YOUR_API_KEY"
os.environ["SERPER_API_KEY"] = "Your Key" # serper.dev API key

# You can choose to use a local model through Ollama for example. See https://docs.crewai.com/how-to/LLM-Connections/ for more information.

# os.environ["OPENAI_API_BASE"] = 'http://localhost:11434/v1'
# os.environ["OPENAI_MODEL_NAME"] ='openhermes'  # Adjust based on available model
# os.environ["OPENAI_API_KEY"] ='sk-111111111111111111111111111111111111111111111111'

search_tool = SerperDevTool()

# Define your agents with roles and goals
researcher = Agent(
  role='Senior Research Analyst',
  goal='Uncover cutting-edge developments in AI and data science',
  backstory="""You work at a leading tech think tank.
  Your expertise lies in identifying emerging trends.
  You have a knack for dissecting complex data and presenting actionable insights.""",
  verbose=True,
  allow_delegation=False,
  tools=[search_tool]
)

writer = Agent(
  role='Tech Content Strategist',
  goal='Craft compelling content on tech advancements',
  backstory="""You are a renowned Content Strategist, known for your insightful and engaging articles.
  You transform complex concepts into compelling narratives.""",
  verbose=True,
  allow_delegation=True
)

# Create tasks for your agents
task1 = Task(
  description="""Conduct a comprehensive analysis of the latest advancements in AI in 2024.
  Identify key trends, breakthrough technologies, and potential industry impacts.""",
  expected_output="Full analysis report in bullet points",
  agent=researcher
)

task2 = Task(
  description="""Using the insights provided, develop an engaging blog
  post that highlights the most significant AI advancements.
  Your post should be informative yet accessible, catering to a tech-savvy audience.
  Make it sound cool, avoid complex words so it doesn't sound like AI.""",
  expected_output="Full blog post of at least 4 paragraphs",
  agent=writer
)

# Instantiate your crew with a sequential process
crew = Crew(
  agents=[researcher, writer],
  tasks=[task1, task2],
  verbose=2, # You can set it to 1 or 2 to different logging levels
)

# Get your crew to work!
result = crew.kickoff()

print("######################")
print(result)
```

<br>
In addition to the sequential process, you can use the hierarchical process, which automatically assigns a manager to the defined crew to properly coordinate the planning and execution of tasks through delegation and validation of results.

<br>
<br>

## License
   CrewAI is released under the MIT License.
