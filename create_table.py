import psycopg2
from cleaning import read_and_clean_results, read_and_clean_shootouts
from create_table import *


#create table in postgres
conn = psycopg2.connect(
    host = "localhost",
    database = "Football",
    user = "postgres",
    password="postgres",
  
)


def create_results_table(cursor):

    
    cursor.execute("""
    DROP TABLE IF EXISTS results;
    CREATE UNLOGGED TABLE results(
    date DATE,
    home_team TEXT,
    away_team TEXT,
    home_score FLOAT,
    away_score FLOAT,
    tournament TEXT,
    city TEXT,
    country TEXT,
    neutral TEXT
    );
    
    """)

cur = conn.cursor()
with conn.cursor() as cursor:
    create_results_table(cursor)


conn.commit()

def create_shootouts_table(cursor):

    
    cursor.execute("""
    DROP TABLE IF EXISTS shootouts;
    CREATE UNLOGGED TABLE shootouts(
    date DATE,
    home_team TEXT,
    away_team TEXT,
    winner TEXT
     );
    
    """)

cur = conn.cursor()
with conn.cursor() as cursor:
    create_shootouts_table(cursor)
conn.commit()



#create csv files
read_and_clean_results()
read_and_clean_shootouts()


#insert data to tables
sql2 = r"COPY results FROM 'C:\Users\Public\results_clean.csv' DELIMITER ',' CSV HEADER;"
cur.execute(sql2)
conn.commit()

sql3 = r"COPY shootouts FROM 'C:\Users\Public\shootouts_clean.csv' DELIMITER ',' CSV HEADER;"
cur.execute(sql3)
conn.commit()

#close the connnection and close cursor
cur.close()
conn.close()