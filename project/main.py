from fastapi import FastAPI
import uvicorn

from project.clients.joke_generator import JokeGeneratorClient
from project.clients.text_translator import TextTranslatorClient

app = FastAPI()


@app.get("/joke/context")
async def get_context() -> list[str]:
    async with JokeGeneratorClient() as client:
        categories: list[str] = await client.get_categories()

    return categories


@app.get("/joke/translate")
async def get_translated_joke(lang: str = 'ru', context: str = 'animal') -> dict:
    async with JokeGeneratorClient() as client:
        joke: dict = await client.get_joke(category=context)

    async with TextTranslatorClient() as client:
        translated_joke: dict = await client.get_translation(
            text=JokeGeneratorClient().extract(joke),
            target_language=lang,
        )

    return translated_joke


if __name__ == '__main__':
    uvicorn.run("main:app")
