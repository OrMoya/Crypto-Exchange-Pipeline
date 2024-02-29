import time
import requests
import pandas as pd
import json
import boto3
import botocore
import logging
import sys

#Endpoint connection string
api_url = "https://api.coincap.io/v2/exchanges"
s3_bucket_name = "crypto-data-raw"


def get_exchange_data():
    try: 
        response = requests.get(api_url)
    except requests.ConnectionError as ce: 
        logging.error(f'There was an error with the request, {ce}')
        sys.exit(1)
    return response.json().get('data',[])

def store_exchange_data_in_s3(data, bucket_name, key):
    s3 = boto3.client("s3")
    try:
        s3.put_object(
            Body=json.dumps(data),
            Bucket=bucket_name,
            Key=key
        )
    except botocore.exceptions.ClientError as error:
        logging.error(f'There was an error with s3: {error}')
        

def run() -> None:
    timestamp_id = str((int(time.time())))
    raw_data = get_exchange_data()
    store_exchange_data_in_s3(raw_data, s3_bucket_name, 'crypto_data_raw' + timestamp_id)





