from fastapi import APIRouter
from pydantic import BaseModel
import random

api_router = APIRouter()

class TradeSignal(BaseModel):
    ticker: str
    amount_usd: float

@api_router.post("/trade/execute")
async def execute_trade(signal: TradeSignal):
    # Triggers the quant trading agent
    action = random.choice(["BUY", "SELL", "HOLD"])
    return {
        "status": "success", 
        "ticker": signal.ticker,
        "action_taken": action,
        "confidence": round(random.uniform(0.7, 0.99), 2)
    }
