from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    X_RAPID_API_KEY = ''

    class Config:
        env_file = '.env'


settings = Settings()
