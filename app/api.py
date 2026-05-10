from fastapi import FastAPI
from pydantic import BaseModel
from app.graph.workflow import run_workflow

app = FastAPI(title = "AI Competitive Intelligence Agent")

class ResearchRequest(BaseModel):
    company:str
    focus:str | None = "general competitive analysis"

class ResearchResponse(BaseModel):
    company:str
    report:str


@app.get("/")
def root():
    return {"status": "running", "message": "AI Competitive Intelligence Agent API"}


@app.post("/research",response_model = ResearchResponse)
async def research(request: ResearchRequest):
    result = run_workflow(company=request.company, focus = request.focus)
    return ResearchResponse(company=request.company,report=result)