from fastapi import FastAPI

app = FastAPI(
    title="Windows AI Network Analyzer",
    version="0.1.0"
)

@app.get("/")
def root():
    return {
        "application": "Windows AI Network Analyzer",
        "status": "running"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }