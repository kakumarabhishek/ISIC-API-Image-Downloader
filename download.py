import argparse
from pathlib import Path
from isic_api_get_images import get_image_by_isic_id

# Define the base URL for the ISIC API v2.
# https://api.isic-archive.com/api/docs/swagger/#/images/isic_core_api_image_retrieve_image
BASE_URL = "https://api.isic-archive.com/api/v2/images/"


def main():
    # Create the parser.
    parser = argparse.ArgumentParser()

    # Add the arguments.
    parser.add_argument(
        "--download_id",
        type=str,
        required=False,
        help="The ISIC ID of the image to download.",
    )
    parser.add_argument(
        "--download_list",
        type=str,
        required=False,
        help="The file containing a list of ISIC IDs to download.",
    )
    parser.add_argument(
        "--output_dir",
        type=str,
        required=True,
        help="The output directory to save the files to.",
    )
    parser.add_argument(
        "--download_images",
        action="store_true",
        help="Download the image file.",
    )
    parser.add_argument(
        "--download_metadata",
        action="store_true",
        help="Download the metadata file.",
    )

    # Parse the arguments.
    args = parser.parse_args()

    # Validate that at least one download option is selected.
    if not (args.download_images or args.download_metadata):
        print("Please specify at least one download option "
              "(--download_images or --download_metadata).")
        return

    # Create the main output directory if it doesn't exist.
    Path(args.output_dir).mkdir(parents=True, exist_ok=True)
    # Create folders for images and metadata if they are to be downloaded.
    if args.download_images:
        Path(args.output_dir, "images").mkdir(parents=True, exist_ok=True)
    if args.download_metadata:
        Path(args.output_dir, "metadata").mkdir(parents=True, exist_ok=True)

    if args.download_id:
        # Download a single image and/or metadata.
        get_image_by_isic_id(
            base_url=BASE_URL,
            isic_id=args.download_id,
            output_dir=args.output_dir,
            download_images=args.download_images,
            download_metadata=args.download_metadata,
        )

    elif args.download_list:
        # Download a list of images and/or metadata.
        with open(args.download_list, "r") as f:
            for line in f:
                isic_id = line.strip()
                get_image_by_isic_id(
                    base_url=BASE_URL,
                    isic_id=isic_id,
                    output_dir=args.output_dir,
                    download_images=args.download_images,
                    download_metadata=args.download_metadata,
                )
    else:
        print("Please provide either --download_id or --download_list.")

    return None


if __name__ == "__main__":
    main()
