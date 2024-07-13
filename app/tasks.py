import logging

from app import celery


@celery.task
def process_image(file_path):
    from logging import getLogger
    logger = getLogger("celery")

    from PIL import Image
    try:
        with Image.open(file_path) as img:
            grayscale_img = img.convert("L")
            processed_file_path = f"processed_{file_path}"
            grayscale_img.save(processed_file_path)

        logger.info(f"Processed {file_path} to {processed_file_path}")
    except Exception as e:
        logger.error(f"Failed to process {file_path}: {str(e)}")
