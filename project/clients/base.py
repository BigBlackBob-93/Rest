from abc import ABC, abstractmethod
from settings import settings
from aiohttp import ClientSession


class APIClient(ABC):
    def __init__(self, x_rapid_api_host: str, url: str):
        self.x_rapid_api_host: str = x_rapid_api_host
        self.url: str = url
        self.headers: dict = {
            "X-RapidAPI-Key": settings.X_RAPID_API_KEY,
            "X-RapidAPI-Host": self.x_rapid_api_host,
        }

    @abstractmethod
    async def extract(self, data: dict):
        pass

    async def __aenter__(self) -> 'APIClient':
        self.client = ClientSession()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        await self.close()

    async def close(self) -> None:
        await self.client.close()
