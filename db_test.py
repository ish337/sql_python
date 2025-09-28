import os
from dotenv import load_dotenv
import pyodbc
from Lib.db_manager import menu

load_dotenv(override=True)

conn_str = os.getenv("conn_str")

conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

menu(cursor, conn)


cursor.close()
conn.close()