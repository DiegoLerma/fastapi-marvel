import hashlib
import time
import os
import requests
import logging

# Configuración básica de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Cargar las credenciales de Marvel desde variables de entorno
MARVEL_PUBLIC_KEY = os.getenv("MARVEL_PUBLIC_KEY")
MARVEL_PRIVATE_KEY = os.getenv("MARVEL_PRIVATE_KEY")


def get_marvel_character(name: str):
    """
    Fetch details about a Marvel character by name from the Marvel API.

    Args:
    - name (str): Name of the Marvel character.

    Returns:
    - dict: Character details from the Marvel API.

    Raises:
    - ValueError: If no character is found or the API returns an error.
    """
    base_url = "http://gateway.marvel.com/v1/public/characters"

    # Timestap y hash para la autenticación
    ts = str(int(time.time()))
    hash_md5 = hashlib.md5(
        f"{ts}{MARVEL_PRIVATE_KEY}{MARVEL_PUBLIC_KEY}".encode("utf-8")
    ).hexdigest()

    # Parámetros de la solicitud
    params = {"name": name, "apikey": MARVEL_PUBLIC_KEY, "ts": ts, "hash": hash_md5}

    try:
        # Hacer la solicitud a la API de Marvel
        response = requests.get(base_url, params=params, timeout=10)
        data = response.json()

        # Registrar detalles completos de la respuesta
        logger.info("Response Status Code: %s", response.status_code)
        logger.info("Response Body: %s", data)

        # Si la solicitud fue exitosa y contiene resultados
        if response.status_code == 200 and data["data"]["results"]:
            return data["data"]["results"][0]
        else:
            # Si no se encuentra el personaje o hay otro error
            logger.error("Marvel API Error: %s", data)
            raise ValueError(f"Character not found or API error: {data}")

    except requests.exceptions.Timeout:
        logger.error("Request timed out")
        raise

    except requests.exceptions.RequestException as e:
        logger.error("Request failed: %s", e)
        raise
