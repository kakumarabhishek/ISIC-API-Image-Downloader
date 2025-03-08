# ISIC API Image Downloader

This script downloads images and their corresponding metadata by ISIC IDs from the [ISIC Archive API v2](https://api.isic-archive.com/api/docs/swagger/).

## Usage

You can either download a single image by its ID by using the `--download_id` and `--download_images` flags:

```python
python download.py --download_id ISIC_0000003 --output_dir output/ --download_images
```

or download multiple images by a list of IDs provided in a text file and the `--download_list` flag:

```python
python download.py --download_list isic_ids.txt --output_dir output/ --download_images
```

or download only the metadata of the images by using the `--download_metadata` flag:

```python
python download.py --download_id ISIC_0000003 --output_dir output/ --download_metadata
```

or download both images and metadata by using the `--download_metadata` flag:

```python
python download.py --download_list isic_ids.txt --output_dir output/ --download_images --download_metadata
```