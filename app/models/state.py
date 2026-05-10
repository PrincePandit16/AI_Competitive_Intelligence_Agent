from typing import TypedDict,List
class GraphState(TypedDict):

    query: str

    tasks: List[str]

    research_data: List[dict]

    summary: str

    verification_report: str

    final_report: str