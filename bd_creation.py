import psycopg2

host = "localhost"
database = "postgres"
user = "postgres"
password = "12345"

connection = psycopg2.connect(host=host, user=user, password=password)
cursor = connection.cursor()
print(connection.get_transaction_status())
connection.close()
