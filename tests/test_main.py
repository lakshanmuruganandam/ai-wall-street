from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "message": "Trading swarm is active and monitoring markets."}

def test_execute_trade():
    response = client.post("/api/v1/trade/execute", json={
        "ticker": "AAPL", 
        "amount_usd": 10000.00
    })
    assert response.status_code == 200
    data = response.json()
    assert data["ticker"] == "AAPL"
    assert data["action_taken"] in ["BUY", "SELL", "HOLD"]
