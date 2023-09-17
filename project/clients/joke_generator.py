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
