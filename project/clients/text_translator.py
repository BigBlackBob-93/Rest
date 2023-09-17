from project.clients.base import APIClient


class TextTranslatorClient(APIClient):
    def __init__(self):
        super().__init__(
            x_rapid_api_host='text-translator2.p.rapidapi.com',
            url='https://text-translator2.p.rapidapi.com/',
        )
        self.headers.update({"content-type": "application/x-www-form-urlencoded"})

    def extract(self, data: dict) -> str:
        return data.get('data').get('translatedText')

    async def get_translation(self, text: str, target_language: str) -> dict[str, str]:
        data: dict = {
            "source_language": "en",
            "target_language": target_language,
            "text": text,
        }

        response = await self.client.post(
            self.url + 'translate',
            data=data,
            headers=self.headers,
        )

        return await response.json()
