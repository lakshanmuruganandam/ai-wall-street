<div align="center">
  <h1>📈 AI Wall Street</h1>
  <p><b>An autonomous, local swarm of quantitative AI agents that analyze markets and trade with zero latency.</b></p>
</div>

## 📖 The Story
Stop trusting random Reddit threads for stock advice. I wanted a personal hedge fund that runs locally on my MacBook. So I built an autonomous swarm of quant agents.

## 🚀 How it Works
1. **The Sentiment Analyst:** Scrapes Twitter and news for market sentiment.
2. **The Technical Analyst:** Analyzes charts and moving averages.
3. **The Executioner:** Merges the data, debates the confidence interval, and outputs a final `BUY/SELL/HOLD` command.

## 🛠️ Quickstart

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn src.main:app --reload
```

Hit `http://127.0.0.1:8000/docs` to start executing trades.

## 🧠 Architecture
- **FastAPI** for sub-millisecond trade orchestration.
- **Pydantic** for strict risk-management validation.
- **Pytest** for ensuring we don't accidentally short the entire market.

## 🤝 Contributing
Want to add a new quant model? Open a PR.

---
*Built with ❤️ by Lakshan Muruganandam*
