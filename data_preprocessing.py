import pandas as pd
import psycopg2

host = "localhost"
database = "postgres"
user = "postgres"
password = "12345"

connection = psycopg2.connect(host=host, database=database, user=user, password=password)
cursor = connection.cursor()
cursor.execute("SELECT * FROM dataset")
data = cursor.fetchall()
cursor.close()
connection.close()

df = pd.DataFrame(data)