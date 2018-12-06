class Database():

    def tables(self):

        db1 = """CREATE TABLE IF NOT EXISTS users(
        user_id serial PRIMARY KEY NOT NULL,
        first_name VARCHAR(50) NOT NULL,
        other_names VARCHAR(50) NOT NULL,
        last_name VARCHAR(50) NOT NULL,
        username VARCHAR(50) NOT NULL,
        email VARCHAR(50) NOT NULL UNIQUE,
        phone_number VARCHAR(13) NOT NULL UNIQUE,
        is_admin BOOLEAN NOT NULL DEFAULT FALSE,
        registered timestamp with time zone DEFAULT \
        ('now'::text):: date NOT NULL,
        password VARCHAR(50) NOT NULL
            )"""

        db2 = """CREATE TABLE IF NOT EXISTS incidents(
        incident_id serial PRIMARY KEY NOT NULL,
        created_on timestamp with time zone DEFAULT\
         ('now'::text):: date NOT NULL,
        created_by numeric NOT NULL,
        type VARCHAR(50) NOT NULL,
        location VARCHAR(100) NOT NULL,
        status VARCHAR(20) NOT NULL DEFAULT Draft,
        comment VARCHAR(2000) NOT NULL,
        user_id INTEGER REFERENCES users(user_id)
            )"""

        self.queries = [db1,db2] 
        return self.queries
    

    def drop_query(self):
        query_users = """DROP TABLE IF EXISTS users"""
        query_incidents = """DROP TABLE IF EXISTS incident""" 
        self.queries = [query_users,query_incidents] 
        return self.queries