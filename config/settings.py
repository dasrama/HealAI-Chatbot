from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    GEMINI_API_TOKEN: str
    DISCORD_BOT_TOKEN: str

    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379

    class Config:
        env_file = ".env"
