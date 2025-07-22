from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    TRONGRID_API_KEY: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings(_env_file=".env")  # pyright: ignore