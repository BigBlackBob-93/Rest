from abc import ABC, abstractmethod
import settings


class APIClient(ABC):
    def __init__(self, x_rapid_api_host: str, url: str):
        self.x_rapid_api_host: str = x_rapid_api_host
        self.url: str = url
        self.headers = {
            "X-RapidAPI-Key": settings.settings.X_RAPID_API_KEY,
            "X-RapidAPI-Host": self.x_rapid_api_host,
        }

    @abstractmethod
    async def extract(self, data: dict):
        pass

