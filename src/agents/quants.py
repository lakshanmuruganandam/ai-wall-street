from pydantic import BaseModel, Field
from typing import List, Dict, Optional
import asyncio

class MarketData(BaseModel):
    ticker: str
    current_price: float
    sentiment_score: float = Field(..., ge=-1.0, le=1.0)
    moving_average_50d: float
    moving_average_200d: float

class AgentAnalysis(BaseModel):
    agent_type: str
    signal: str
    confidence: float

class TradeExecution(BaseModel):
    ticker: str
    action: str
    confidence: float
    reasoning: str
    sub_analysis: List[AgentAnalysis]

class QuantSwarm:
    def __init__(self):
        self.fund_name = "AI Wall Street Local Fund"

    async def _analyze_sentiment(self, data: MarketData) -> AgentAnalysis:
        await asyncio.sleep(0.05)
        signal = "BULLISH" if data.sentiment_score > 0.5 else ("BEARISH" if data.sentiment_score < -0.5 else "NEUTRAL")
        return AgentAnalysis(agent_type="Sentiment Analyst", signal=signal, confidence=abs(data.sentiment_score))

    async def _analyze_technicals(self, data: MarketData) -> AgentAnalysis:
        await asyncio.sleep(0.05)
        # Simple golden cross / death cross logic
        if data.moving_average_50d > data.moving_average_200d:
            return AgentAnalysis(agent_type="Technical Analyst", signal="BULLISH", confidence=0.85)
        else:
            return AgentAnalysis(agent_type="Technical Analyst", signal="BEARISH", confidence=0.80)

    async def analyze_and_trade(self, data: MarketData) -> TradeExecution:
        sentiment_agent, tech_agent = await asyncio.gather(
            self._analyze_sentiment(data),
            self._analyze_technicals(data)
        )
        
        await asyncio.sleep(0.1) # Risk Management Agent Review
        
        signals = [sentiment_agent.signal, tech_agent.signal]
        
        if signals.count("BULLISH") == 2:
            action = "BUY"
            confidence = (sentiment_agent.confidence + tech_agent.confidence) / 2
            reason = "Unanimous bullish consensus across technical and sentiment analysis."
        elif signals.count("BEARISH") == 2:
            action = "SELL"
            confidence = (sentiment_agent.confidence + tech_agent.confidence) / 2
            reason = "Unanimous bearish consensus. Initiating short/sell protocol."
        else:
            action = "HOLD"
            confidence = 0.50
            reason = "Mixed signals between agents. Risk management override applied."
            
        return TradeExecution(
            ticker=data.ticker,
            action=action,
            confidence=confidence,
            reasoning=reason,
            sub_analysis=[sentiment_agent, tech_agent]
        )
