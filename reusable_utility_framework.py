import boto3, logging, time
from botocore.exceptions import ClientError

logging.basicConfig(level=logging.INFO)
def retry(func, retries=3, delay=2):
    for _ in range(retries):
        try:
            return func()
        except ClientError as e:
            logging.warning(f"Retrying due to error: {e}")
            time.sleep(delay)
    raise Exception("Max retries exceeded")

def create_s3_bucket(bucket_name):
    s3 = boto3.client('s3')
    retry(lambda: s3.create_bucket(Bucket=bucket_name))
    logging.info(f"Bucket {bucket_name} created successfully")
