from pydantic import BaseModel, Field

class TradeSignal(BaseModel):
    ticker: str = Field(..., description="Stock ticker symbol")
    amount_usd: float = Field(..., description="USD allocation for this trade block")

class ExecutionOutput(BaseModel):
    ticker: str
    action: str
    confidence: float
    sentiment_score: float
