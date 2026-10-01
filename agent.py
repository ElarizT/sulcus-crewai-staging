from crewai import Agent, BaseLLM, Crew, Process, Task


class DeterministicLLM(BaseLLM):
    def __init__(self):
        super().__init__(
            model="sulcus-deterministic",
            temperature=0.0,
        )

    def call(
        self,
        messages,
        tools=None,
        callbacks=None,
        available_functions=None,
        **kwargs,
    ):
        return "CrewAI staging result: completed"


agent = Agent(
    role="Staging Agent",
    goal="Complete a deterministic Sulcus staging task",
    backstory="A minimal agent used only to validate CrewAI instrumentation.",
    llm=DeterministicLLM(),
    verbose=False,
)

task = Task(
    description="Return a deterministic staging result.",
    expected_output="CrewAI staging result: completed",
    agent=agent,
)

crew = Crew(
    agents=[agent],
    tasks=[task],
    process=Process.sequential,
    verbose=False,
)

result = crew.kickoff()

print(f"CrewAI staging result: {result}")
