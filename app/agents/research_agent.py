from dotenv import load_dotenv
load_dotenv()
from app.prompts.research_prompt import RESEARCH_PROMPT
from app.models.state import GraphState
from app.tools.search_tool import search_web
from app.llms.google_llm import get_llm
llm=get_llm()



def research_node(state:GraphState):
    tasks = state['tasks']
    all_research = []
    for task in tasks:
        search_results = search_web(task)
        combined_data = "\n\n".join([r['content'] for r in search_results])
        prompt = f"""
            "Research prompt":{RESEARCH_PROMPT}
            "task":{task}
            "researched_data":{combined_data}
        """
        response = llm.invoke(prompt)
        all_research.append({
            "task":task,
            "sources":search_results,
            "analysis":response.content
        })
    return {"research_data":all_research}

