import psycopg2

connection = psycopg2.connect(user="new_user1", password = "password", host="127.0.0.1", port="5432", database="database1")
cursor = connection.cursor()

create_table_query = '''CREATE TABLE mobile
            (ID INT PRIMARY KEY     NOT NULL,
            MODEL           TEXT    NOT NULL,
            PRICE           REAL);'''

cursor.execute(create_table_query)
connection.commit()
