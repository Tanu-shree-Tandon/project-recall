from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Project(BaseModel):
    title: str
    author: str

@app.post("/projects")
def create_project(project: Project):
    return {
        "message": "Project created successfully!",
        "project": project
    }
@app.get("/")
def root():
    return {
        "project": "Project Recall",
        "developer": "Tanu",
        "status": "Building MVP",
        "day": 2
    }
@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "server": "running"
    }
@app.get("/about")
def about():
    return {
        "application": "Project Recall",
        "purpose": "AI-powered research context reconstruction",
        "hackathon": "ML Empowerment Build Challenge",
        "version": "0.1.0"
    }
@app.get("/project")
def project():
    return {
        "name": "Project Recall",
        "current_phase": "Backend Fundamentals",
        "current_goal": "Learning FastAPI routing",
        "next_feature": "PDF Upload"
    }
@app.get("/documents/{document_id}")
def get_document(document_id: int):
    print("Function Executed!")

    return {
        "message": "Document found",
        "document_id": document_id
    }
@app.get("/search")
def search(query: str):
    return {
        "search_query": query,
        "message": f"Searching Project Recall for '{query}'"
    }