import os
from dotenv import load_dotenv
import pyodbc
from Lib.db_manager import select_all, create_user, delete_user

load_dotenv(override=True)

conn_str = os.getenv("conn_str")

conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

# select_all(cursor)
# create_user(cursor, conn)
delete_user(cursor, conn)

cursor.close()
conn.close()