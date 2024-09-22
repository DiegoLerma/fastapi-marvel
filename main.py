from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import services

app = FastAPI(title="Marvel API", description="API to fetch Marvel data")


class MarvelCharacterRequest(BaseModel):
    name: str


@app.get("/")
def read_root():
    return {"message": "Welcome to the Marvel API!"}


@app.post("/character/")
async def get_character(character: MarvelCharacterRequest):
    try:
        response = services.get_marvel_character(character.name)
        return response
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) from e
