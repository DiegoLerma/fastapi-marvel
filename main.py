from fastapi import FastAPI, HTTPException

from models import MarvelCharacterRequest, MarvelCharacterResponse
import services

app = FastAPI(
    title="Marvel API",
    description="API to fetch data from the Marvel universe",
    version="1.0.0",
)


@app.get("/", summary="Root endpoint", tags=["Root"])
def read_root():
    """
    Root endpoint for the API.

    Returns a welcome message.
    """
    return {"message": "¡Bienvenido al proyecto de FastAPI x Marvel de Diego Lerma para LiteThinking!"}


@app.post(
    "/character/",
    response_model=MarvelCharacterResponse,
    summary="Fetch Marvel character",
    tags=["Character"],
)
async def get_character(character: MarvelCharacterRequest):
    """
    Fetch information about a Marvel character by name.

    - **name**: The name of the Marvel character you want to retrieve.

    Returns character details including description, comics, series, and more.
    """
    try:
        response = services.get_marvel_character(character.name)
        return response
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) from e
