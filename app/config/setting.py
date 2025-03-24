from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    GEMINI_API_TOKEN: str
    DISCORD_BOT_TOKEN: str

    class config:
        env_file = ".env"
