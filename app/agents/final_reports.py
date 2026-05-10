from app.models.state import GraphState
from app.llms.groq_llm import get_llm
from dotenv import load_dotenv
load_dotenv()
llm=get_llm()
def final_report(state:GraphState):
    verified = state['verification_report']
    prompt = f"""
    generate a final report using the verification report:{verified}
    """
    response = llm.invoke(prompt)
    return {"final_report":response.content}