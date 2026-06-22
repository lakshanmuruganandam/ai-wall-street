import pytest
from src.agents.quants import QuantSwarm, MarketData

@pytest.mark.asyncio
async def test_quant_buy_execution():
    swarm = QuantSwarm()
    bull_market = MarketData(
        ticker="NVDA", 
        current_price=120.50, 
        sentiment_score=0.9,
        moving_average_50d=110.0,
        moving_average_200d=95.0
    )
    
    decision = await swarm.analyze_and_trade(bull_market)
    
    assert decision.ticker == "NVDA"
    assert decision.action == "BUY"
    assert decision.confidence >= 0.85
    assert len(decision.sub_analysis) == 2

@pytest.mark.asyncio
async def test_quant_hold_execution():
    swarm = QuantSwarm()
    mixed_market = MarketData(
        ticker="TSLA", 
        current_price=200.00, 
        sentiment_score=-0.8,  # Bearish sentiment
        moving_average_50d=210.0,
        moving_average_200d=190.0  # Bullish technicals
    )
    
    decision = await swarm.analyze_and_trade(mixed_market)
    
    assert decision.action == "HOLD"
    assert "Mixed signals" in decision.reasoning
