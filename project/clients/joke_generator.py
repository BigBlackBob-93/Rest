from project.clients.base import APIClient


class JokeGeneratorClient(APIClient):
    def __init__(self):
        super().__init__(
            x_rapid_api_host='matchilling-chuck-norris-jokes-v1.p.rapidapi.com',
            url='https://matchilling-chuck-norris-jokes-v1.p.rapidapi.com/jokes/',
        )
        self.headers.update({"accept": "application/json"})

    def extract(self, data: dict) -> str:
        return data.get('value')

    async def get_categories(self) -> list[str]:
        response = await self.client.get(
            self.url + 'categories',
            headers=self.headers,
        )

        return await response.json()

    async def get_joke(self, category: str) -> dict[str, str]:
        response = await self.client.get(
            self.url + 'random',
            headers=self.headers,
            params={"category": category},
        )

        return await response.json()
