import json 
import boto3
import botocore
import psycopg2.extras

from util.db import DatabaseConnection
from util.db_config import get_database_creds
from util.util import get_most_recent_s3_object, get_utc_from_unix_time
from typing import Any, Dict

#
bucket_name = 'crypto-data-raw'
key_name = get_most_recent_s3_object('crypto-data-raw', 'crypto_data_raw')['Key']

def exchange_insert_query() -> str:
    return  '''
    INSERT INTO public.exchanges (
        coinid,
        name,
        rank,
        percenttotalvolume,
        volumeusd,
        tradingpairs,
        socket,
        exchangeurl,
        updated_unix_millis,
        updated_utc,
        upload_utc
    )
    VALUES (
        %(exchangeId)s,
        %(name)s,
        %(rank)s,
        %(percentTotalVolume)s,
        %(volumeUsd)s,
        %(tradingPairs)s,
        %(socket)s,
        %(exchangeUrl)s,
        %(updated)s,
        %(update_dt)s,
        now()::timestamp
    );
'''

def get_exchange_data_from_s3(bucket_name, key_name):
    s3 = boto3.resource('s3')
    s3_object = s3.Object(bucket_name, key_name)
    data = s3_object.get()['Body'].read().decode('utf-8')
    data = json.loads(data)
    return data

def run() -> None:
    data = get_exchange_data_from_s3(bucket_name,key_name)
    for d in data: 
        d['update_dt'] = get_utc_from_unix_time(d.get('updated'))
    with DatabaseConnection(get_database_creds()).managed_cursor() as curr:
        psycopg2.extras.execute_batch(curr, exchange_insert_query(), data)

