from langgraph.graph import StateGraph, START, END
from app.agents.research_agent import research_node
from app.agents.planner_agent import planner_node
from app.agents.summarizer_agent import summarize_node
from app.agents.verifier_agent import verify_node
from app.agents.final_reports import final_report
from app.models.state import GraphState

graph = StateGraph(GraphState)
graph.add_node("planner_node",planner_node)
graph.add_node("research_node",research_node)
graph.add_node("verification_node",verify_node)
graph.add_node("summarize_node",summarize_node)
graph.add_node("final_node",final_report)


graph.add_edge(START,"planner_node")
graph.add_edge("planner_node","research_node")
graph.add_edge("research_node","summarize_node")
graph.add_edge("summarize_node","verification_node")
graph.add_edge("verification_node","final_node")
graph.add_edge("final_node",END)

graph = graph.compile()

def run_workflow(company: str, focus: str) -> str:
    query = f"{company} - {focus}"
    result = graph.invoke({"query": query})
    return result["final_report"] 