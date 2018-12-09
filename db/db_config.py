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
    
def close_connection(conn):
    """Closes connection after queries"""
    conn.commit()
    conn.close()

def create_tables():
    """Creates the Tables"""
    con = connection(url)
    cursor = con.cursor()

    database = Database()
    queries = database.tables()

    for query in queries:        
        cursor.execute(query)
    close_connection(con)

def create_default_admin():
    """This function creates a default admin"""

    con = connection(url)
    cursor = con.cursor()

    f_name = 'admin'
    o_name = 'admin'
    l_name = 'admin'
    username = 'adminuser'
    email = 'admin@gmail.com'
    phonenumber = '0711111111'
    password = 'adminstrator'
    is_admin = True 

    sql = "SELECT * FROM users WHERE username = %s"
    cursor.execute(sql, (username,))
    data = cursor.fetchone()

    if not data:
        sql = 'INSERT INTO users(f_name,o_name,l_name,username,email,\
        phonenumber,is_admin,password) VALUES(%s,%s,%s,%s,%s,%s)'
        cursor.execute(sql, (f_name,o_name,l_name,username,email,phonenumber,is_admin,password))
    close_connection(con)


def drop_tables():
    """Drop tables"""
    con = connection(url)
    cursor = con.cursor()

    database = Database()
    queries = database.drop_query()


    for query in queries:        
        cursor.execute(query)
    close_connection(con)


