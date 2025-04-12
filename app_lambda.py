import boto3
import os
from PIL import Image

s3 = boto3.client('s3')
output_bucket = os.environ['OUTPUT_BUCKET']

def lambda_handler(event, context):
    for record in event['Records']:
        source_bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        download_path = f'/tmp/{os.path.basename(key)}'
        s3.download_file(source_bucket, key, download_path)

        with Image.open(download_path) as img:
            base_name = os.path.splitext(os.path.basename(key))[0]
            for fmt in ['BMP', 'GIF', 'PNG']:
                output_path = f'/tmp/{base_name}.{fmt.lower()}'
                img.save(output_path, fmt)
                s3.upload_file(output_path, output_bucket, os.path.basename(output_path))
                os.remove(output_path)
        os.remove(download_path)
