from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200

def test_execute_trade():
    response = client.post("/api/v1/trade/execute", json={
        "ticker": "AAPL", 
        "amount_usd": 10000.00
    })
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert "trade" in data
    assert data["trade"]["ticker"] == "AAPL"
    assert data["trade"]["action"] in ["BUY", "SELL", "HOLD"]
    assert "confidence" in data["trade"]
    assert "sentiment_score" in data["trade"]
