import json
import logging
import etl_extract
import etl_load

def lambda_handler(event, context):
    if etl_extract.run():
        etl_load.run()
        return{
            'statusCode':200,
            'body': json.dumps('Success!')
        }
    else:
        return {
            'statusCode': 400,
            'body': json.dumps('Error: ETL Pipeline did not run!')
        }

lambda_handler(None,None)