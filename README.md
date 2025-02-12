# ISIC API Image Downloader

This script downloads images by ISIC IDs from the [ISIC Archive API v2](https://api.isic-archive.com/api/docs/swagger/).

## Usage

You can either download a single image by its ID:

```python
python download.py --download_id ISIC_0000003 --output_dir images/
```

or download multiple images by a list of IDs provided in a text file:

```python
python download.py --download_list isic_ids.txt --output_dir images/
```