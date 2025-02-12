import os
from pathlib import Path
import requests
import urllib.request


def get_image_by_isic_id(
    base_url: str, isic_id: os.PathLike, output_dir: os.PathLike
) -> None:
    """Download an image by its ISIC ID.

    Args:
        base_url: The base URL of the ISIC API.
        isic_id: The ISIC ID of the image to download.
        output_dir: The directory to save the image to.

    Returns:
        None
    """

    # Create the URL to download the image from.
    img_url = f"{base_url}{isic_id}"

    # Get the JSON response from the API.
    response = requests.get(img_url)
    response.raise_for_status()

    # Get the image URL from the JSON response.
    img_url = response.json()["files"]["full"]["url"]

    # Download the image.
    img_path = Path(output_dir) / f"{isic_id}.jpg"
    urllib.request.urlretrieve(img_url, img_path)

    return None
