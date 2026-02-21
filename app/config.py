from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str = "postgresql://postgres:postgres@localhost:5432/orders_db"
    redis_url: str = "redis://localhost:6379/0"
    env: str = "development"
    app_name: str = "Order Processing API"
    api_v1_prefix: str = "/api/v1"

    class Config:
        env_file = ".env"


settings = Settings()
