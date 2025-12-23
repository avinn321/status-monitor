from fastapi import FastAPI

app = FastAPI(title="Log Monitor SaaS")

@app.get("/health")
def health():
    return {
        "status": "ok"
    }
