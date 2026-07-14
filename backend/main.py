from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {
        "project": "Project Recall",
        "developer": "Tanu",
        "status": "Building MVP",
        "day": 2
    }