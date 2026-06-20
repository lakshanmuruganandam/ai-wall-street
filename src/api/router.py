from fastapi import APIRouter
from src.models.quant import TradeSignal, ExecutionOutput
from src.services.agent import QuantAgentSwarm

api_router = APIRouter()
swarm = QuantAgentSwarm()

@api_router.post("/trade/execute", response_model=dict)
async def execute_trade(signal: TradeSignal):
    execution = await swarm.execute_trade(signal)
    return {
        "status": "success", 
        "trade": execution.model_dump()
    }
