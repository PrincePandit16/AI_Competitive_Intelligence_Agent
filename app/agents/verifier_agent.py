from app.models.state import GraphState
from app.prompts.verification_prompt import VERIFICATION_PROMPT
from app.llms.huggingface_llm import get_llm
llm= get_llm()



def verify_node(state: GraphState):

    summaries = state['summary']

    prompt = f"""
        {VERIFICATION_PROMPT}

        Research Content:
        {summaries}
    """

    response = llm.invoke(prompt)

    return {
        "verification_report": response.content
    }