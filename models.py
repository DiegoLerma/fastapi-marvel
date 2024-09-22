from pydantic import BaseModel, Field


class MarvelCharacterRequest(BaseModel):
    """
    Schema for the request to fetch a Marvel character.

    Attributes:
    - name: The name of the Marvel character (minimum 2 characters).
    """

    name: str = Field(
        ..., min_length=2, description="The name of the Marvel character you want to retrieve."
    )

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Spider-Man (Miles Morales)"
            }
        }


class MarvelCharacterResponse(BaseModel):
    """
    Schema for the response containing details about the Marvel character.

    Attributes:
    - id: Character ID from the Marvel API.
    - name: Name of the Marvel character.
    - description: Description of the character.
    - thumbnail: URL of the character's thumbnail image.
    - resourceURI: URI for further details about the character.
    - comics: List of comics the character appears in.
    - series: List of series the character appears in.
    """

    id: int = Field(..., description="The unique identifier of the Marvel character.")
    name: str = Field(..., description="The name of the Marvel character.")
    description: str = Field(..., description="A brief description of the character.")
    thumbnail: dict = Field(..., description="Thumbnail image details.")
    resourceURI: str = Field(
        ..., description="URI to access detailed character information."
    )
    comics: dict = Field(..., description="Comics in which the character has appeared.")
    series: dict = Field(..., description="Series in which the character has appeared.")

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1016181,
                "name": "Spider-Man (Miles Morales)",
                "description": "Teenager Miles Morales grew up in Brooklyn, New York...",
                "thumbnail": {
                    "path": "http://i.annihil.us/u/prod/marvel/i/mg/f/50/537bcfa1eed73",
                    "extension": "jpg",
                },
                "resourceURI": "http://gateway.marvel.com/v1/public/characters/1016181",
                "comics": {
                    "available": 465,
                    "collectionURI": "http://gateway.marvel.com/v1/public/characters/1016181/comics",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/58636",
                            "name": "Marvel New Year's Eve Special Infinite Comic (2017) #1",
                        }
                    ],
                },
                "series": {
                    "available": 132,
                    "collectionURI": "http://gateway.marvel.com/v1/public/characters/1016181/series",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/27272",
                            "name": "Absolute Carnage (2019)",
                        }
                    ],
                },
            }
        }
