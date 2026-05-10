from app.models.state import GraphState
from app.llms.google_llm import get_llm
from dotenv import load_dotenv
from app.prompts.summary_prompt import SUMMARY_PROMPT
load_dotenv()


llm = get_llm()

def summarize_node(state:GraphState):
    researched_data = state['research_data']
    combined = "\n\n".join(r['analysis'] for r in researched_data)
    prompt = f"""
    "research_data":{combined}
    "summary_prompt":{SUMMARY_PROMPT}
    """
    response = llm.invoke(prompt)
    return {"summary":response.content}