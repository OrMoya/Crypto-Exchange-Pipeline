import psycopg2
import os
from contextlib import contextmanager
from dataclasses import dataclass 
from dotenv import load_dotenv

@dataclass
class DBConnection:
    db: str
    user: str
    password: str
    host: str
    port: int = 5432

class DatabaseConnection:
    def __init__(self, db_conn: DBConnection):
        self.con_url = (
            f'postgresql://{db_conn.user}:{db_conn.password}@'
            f'{db_conn.host}:{db_conn.port}/{db_conn.db}'
        )

    @contextmanager
    def managed_cursor(self, cursor_factory=None):
        self.conn = psycopg2.connect(self.con_url)
        self.conn.autocommit = True
        self.curr = self.conn.cursor(cursor_factory=cursor_factory)
        try:
            yield self.curr
        finally:
            self.curr.close()
            self.conn.close()