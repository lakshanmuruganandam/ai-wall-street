from fastapi import FastAPI
from src.agents.quants import QuantSwarm, MarketData, TradeExecution

app = FastAPI(title="AI Wall Street", version="1.0.0")
swarm = QuantSwarm()

@app.post("/trade", response_model=TradeExecution)
async def execute_trade(data: MarketData):
    """
    Submits market data to the quant swarm for analysis and execution.
    """
    decision = await swarm.analyze_and_trade(data)
    return decision

@app.get("/health")
def health_check():
    return {"status": "Markets are open. Swarm is active."}
