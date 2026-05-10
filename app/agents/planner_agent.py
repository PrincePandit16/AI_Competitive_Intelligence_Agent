from app.prompts.planner_prompt import PLANNER_PROMPT
from dotenv import load_dotenv
import json
from app.models.state import GraphState
from app.llms.groq_llm import get_llm

load_dotenv()
llm=get_llm()


def planner_node(state: GraphState):

    prompt = PLANNER_PROMPT.format(
        query=state["query"]
    )

    response = llm.invoke(prompt)

    content = response.content.strip()

    print("\nRAW LLM RESPONSE:\n")
    print(content)

    content = content.replace("```json", "")
    content = content.replace("```", "")

    tasks = json.loads(content)

    return {
        "tasks": tasks
    }