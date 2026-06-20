from fastapi import FastAPI
from src.api.router import api_router

app = FastAPI(
    title="AI Wall Street",
    description="Autonomous AI Trading Swarm & Market Sentiment Analyzer",
    version="1.0.0"
)

app.include_router(api_router, prefix="/api/v1")

@app.get("/health")
def health_check():
    return {"status": "ok", "message": "Trading swarm is active and monitoring markets."}
