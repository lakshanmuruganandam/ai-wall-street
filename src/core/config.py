from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "AI Wall Street Quant Swarm"
    environment: str = "production"
    risk_tolerance: float = 0.5
    
    class Config:
        env_file = ".env"

settings = Settings()
