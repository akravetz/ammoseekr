import argparse
import io
import json
import logging
import os
from datetime import datetime

from google.cloud import storage
from pydantic_core import to_jsonable_python

import ammoseekr


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Sample application with --dry-run support.")
    parser.add_argument('--dry-run', action='store_true', help='Run the application without making changes.')
    parser.add_argument('--verbose', action='store_true', help='Set log level to INFO')
    return parser.parse_args()

def upload_to_cloud(bucket_name: str, file_path: str, data: str) -> None:
    cli = storage.Client()
    bucket = cli.get_bucket(bucket_name)
    blob = bucket.blob(file_path)

    string_buffer = io.BytesIO(data.encode('utf-8'))
    blob.upload_from_file(string_buffer)


def main():
    args = parse_args()
    if args.verbose:
        logging.basicConfig(level=logging.INFO)
    try:
        BUCKET_NAME = os.environ['BUCKET_NAME']
    except KeyError:
        logging.error('BUCKET_NAME environment variable must be set')
        return
    
    
    if 'GOOGLE_APPLICATION_CREDENTIALS' not in os.environ:
        logging.error('service account credentials file must be set via GOOGLE_APPLICATION_CREDENTIALS environment variable')
        return
    
    logging.info('listing deals')
    s = ammoseekr.Scraper(caliber=ammoseekr.PISTOL_9MM)
    res = s.list_deals()
    
    json_text = json.dumps(to_jsonable_python(res))
    
    filename = datetime.now().strftime("%Y%m%d-%H%M%S_9mm.json")

    if args.dry_run:
        logging.info(f'DRY RUN: would upload results to {BUCKET_NAME}/{filename}')
    else:
        upload_to_cloud(
            BUCKET_NAME,
            filename,
            json_text
        )


if __name__ == "__main__":
    main()
