import pytest
from src.agents.quants import QuantSwarm, MarketData

@pytest.mark.asyncio
async def test_quant_trade_execution():
    swarm = QuantSwarm()
    bull_market = MarketData(ticker="NVDA", current_price=120.50, sentiment_score=0.9)
    
    decision = await swarm.analyze_and_trade(bull_market)
    
    assert decision.ticker == "NVDA"
    assert decision.action == "BUY"
    assert decision.confidence > 0.9
