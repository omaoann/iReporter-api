import os
import psycopg2
from .db_model import Database


url = "dbname='ireporter_test' host='localhost' \
     port='5432' user='postgres' password='naivasha_234'"

#url = os.getenv('DATABASE_URL')

def connection(url):
    """Create Database Connection"""
    conn = psycopg2.connect(url)
    return conn

def init_db():
    conn = connection(url)
    return conn


def create_tables():
    """Creates the Tables"""
    con = connection(url)
    cursor = con.cursor()

    database = Database()
    queries = database.tables()

    for query in queries:        
        cursor.execute(query)
    con.commit()

def drop_tables():
    """Drop tables"""
    con = connection(url)
    cursor = con.cursor()

    database = Database()
    queries = database.drop_query()


    for query in queries:        
        cursor.execute(query)
    con.commit()  


if __name__ == "__main__":
    drop_tables()