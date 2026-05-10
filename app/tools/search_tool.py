from tavily import TavilyClient
from dotenv import load_dotenv
load_dotenv()
import os


client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

def search_web(query:str,max_results:int=5):
    response = client.search(query=query,search_depth='advanced',max_results=max_results)
    result=[]
    for r in response["results"]:
        result.append({
            "title":r["title"],
            "content":r["content"],
            "url":r["url"]
        })
    return result