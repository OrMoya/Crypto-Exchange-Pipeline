import json
import logging
from cryptocoindatapipeline.etl_extract import extract_run
from cryptocoindatapipeline.etl_load import load_run

def lambda_handler(event, context):
    try:
        etl_extract.run()
        etl_load.run()
        return {
            'statusCode': 200,
            'body': json.dumps('sucess!')
        }
    except:
        return {
            'statusCode': 200,
            'body': json.dumps('Error: ETL Pipeline did not run!')
        }
        