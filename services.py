import hashlib
import time
import os
import requests
import logging

# Configuración básica de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Necesitamos cargar las credenciales de Marvel (public_key, private_key)
MARVEL_PUBLIC_KEY = os.getenv("MARVEL_PUBLIC_KEY")
MARVEL_PRIVATE_KEY = os.getenv("MARVEL_PRIVATE_KEY")

logger.info(f"Public Key: {MARVEL_PUBLIC_KEY}, Private Key: {MARVEL_PRIVATE_KEY}")


def get_marvel_character(name: str):
    # Marvel API Base URL
    base_url = "http://gateway.marvel.com/v1/public/characters"

    # Timestap, hash y autenticación
    ts = str(int(time.time()))  # Cambia el timestamp a un entero
    hash_md5 = hashlib.md5(
        f"{ts}{MARVEL_PRIVATE_KEY}{MARVEL_PUBLIC_KEY}".encode("utf-8")
    ).hexdigest()

    # Parámetros de la solicitud
    params = {"name": name, "apikey": MARVEL_PUBLIC_KEY, "ts": ts, "hash": hash_md5}
    logger.info(f"URL: {base_url}, Params: {params}")

    try:
        # Hacer la solicitud a la API de Marvel
        response = requests.get(base_url, params=params, timeout=10)
        data = response.json()

        # Registrar detalles completos de la respuesta
        logger.info(f"Response Status Code: {response.status_code}")
        logger.info(f"Response Body: {data}")

        # Si la solicitud fue exitosa y contiene resultados
        if response.status_code == 200 and data["data"]["results"]:
            return data["data"]["results"][0]
        else:
            # Si no se encuentra el personaje o hay otro error
            logger.error(f"Marvel API Error: {data}")
            raise ValueError(f"Character not found or API error: {data}")

    except requests.exceptions.Timeout:
        logger.error("Request timed out")
        raise

    except requests.exceptions.RequestException as e:
        logger.error(f"Request failed: {e}")
        raise
