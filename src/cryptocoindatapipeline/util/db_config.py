import os
from dotenv import load_dotenv
from cryptocoindatapipeline.util.db import DBConnection
import psycopg2.extras as p

load_dotenv()

def get_database_creds() -> DBConnection:
    return DBConnection(
        user=os.getenv('POSTGRES_USERNAME',''),
        password=os.getenv('POSTGRES_PASSWORD', ''),
        db=os.getenv('POSTGRES_DB', ''),
        host=os.getenv('POSTGRES_HOSTNAME', ''), 
        port=os.getenv('POSTGRES_PORT=', '')
    )
