import psycopg2
from sqlalchemy import create_engine
import pandas as pd
import query
import os


def csv_to_table(database_credentials):
    df1 = pd.read_csv(r'.\movies_csv\movies.csv')
    df2 = pd.read_csv(r'.\movies_csv\ratings.csv')

    try:
        print('creating tables')
        engine = create_engine(f"postgresql://{database_credentials['user']}:{database_credentials['password']}@{database_credentials['host']}:{database_credentials['port']}/{database_credentials['database']}")
        df1.to_sql('movies', con=engine, if_exists='replace', index=False)
        df2.to_sql('ratings', con=engine, if_exists='replace', index=False)
        print("created successfully.")
    except Exception as error:
        print("Error connecting database:", error)
    return 

def sql_queries(database_credentials,query):
    try:
        connection = psycopg2.connect(database_credentials)
        cursor = connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)

    except Exception as error:
        print("Error connecting to PostgreSQL database:", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed.")

if __name__ == "__main__":
      if not os.path.exists('movies_csv'):
        os.mkdir('movies_csv')
     
     
      database_credentials = {
        'host': 'dpg-clq5lapjvg7s73e3br5g-a.oregon-postgres.render.com',
        'database': 'data_analysis',
        'user': 'root',
        'password': 'fDa4ejFPnz1AVIgAEL6uzAwLNvtcx4Dz',
        'port' : "5432"
    }
      con_url = f"postgresql://{database_credentials['user']}:{database_credentials['password']}@{database_credentials['host']}:{database_credentials['port']}/{database_credentials['database']}"

      csv_to_table(database_credentials)
      for i in query.queries:
          
        sql_queries(con_url,i)


