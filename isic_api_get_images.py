import os
from pathlib import Path
import requests
import urllib.request
import json


def get_image_by_isic_id(
    base_url: str,
    isic_id: os.PathLike,
    output_dir: os.PathLike,
    download_images: bool,
    download_metadata: bool,
) -> None:
    """Download an image and/or metadata by its ISIC ID.

    Args:
        base_url: The base URL of the ISIC API.
        isic_id: The ISIC ID of the image to download.
        output_dir: The directory to save the files to.
        download_images: Whether to download the image.
        download_metadata: Whether to download the metadata.

    Returns:
        None
    """

    # Create the URL to download the image from.
    img_url = f"{base_url}{isic_id}"

    # Get the JSON response from the API.
    response = requests.get(img_url)
    response.raise_for_status()

    # Get the JSON response data
    json_data = response.json()

    if download_images:
        # Get the image URL from the JSON response.
        img_url = json_data["files"]["full"]["url"]
        # Download the image.
        img_path = Path(output_dir) / f"images/{isic_id}.jpg"
        urllib.request.urlretrieve(img_url, img_path)

    if download_metadata:
        # Get the metadata from the JSON response.
        metadata = json_data["metadata"]
        # Save the metadata as JSON.
        metadata_path = Path(output_dir) / f"metadata/{isic_id}.json"
        with open(metadata_path, "w") as f:
            json.dump(metadata, f, indent=4)

    return None
