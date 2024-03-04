import json
import logging
from cryptocoindatapipeline.etl_extract import extract_run
from cryptocoindatapipeline.etl_load import load_run

def lambda_handler(event, context):
    etl_extract.run()
    etl_load.run()
    return {
        'statusCode': 400,
        'body': json.dumps('Error: ETL Pipeline did not run!')
    }
