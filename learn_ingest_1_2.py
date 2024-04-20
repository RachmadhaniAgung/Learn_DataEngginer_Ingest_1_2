#1. memastikan keberadaan file ada atau tidak
import pandas as pd
import os.path
import psycopg2
from sqlalchemy import create_engine

datamanusia ="data_manusia.csv"
#2. Pastikan file tersebut dapat diakses atau cek jumlah rows dan colum
dataframe = pd.read_csv("data_manusia.csv")
print(dataframe)

if os.path.exists(datamanusia):
    dataframe = pd.read_csv("data_manusia.csv")
    print(dataframe)

    #3. Konfigurasi koneksi ke PostgreSQL
    host="localhost"
    port=5433
    database="postgres"
    user="postgres"
    password="admin"
    
    #3.1 Create posgrest clinet
    conn = psycopg2.connect( dbname = database, user = user, host = host, password = password, port = port)

    #3.2 Create cursor
    cur = conn.cursor()
    
    #3.3 eksekusi query to create a database
    cur.execute("select * from information_schema.tables where table_name=%s", ('manusia',))
    bool(cur.rowcount)
    print(cur.rowcount)

    #4. insert data
    conn_string = 'postgresql://postgres:admin@localhost:5433/postgres'
    db = create_engine(conn_string) 
    sqlalcemyconn = db.connect()
    dataframe.to_sql('manusia', con=sqlalcemyconn, if_exists='replace', index=True) 

    #5. Menyimpan data ke dalam file Excel
    nama_file_excel = "data_manusia.xlsx"
    dataframe.to_excel(nama_file_excel, index=True)
else :
    print("maap gak ada")


