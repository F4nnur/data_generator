import psycopg2


def insert_into_db(table_name, data):
    connection = psycopg2.connect(user="postgres",
                                  password="postgres",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="data_feed")
    cur = connection.cursor()

    try:
        placeholders = ', '.join(['%s'] * len(data))
        columns = ', '.join(data.keys())
        sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        cur.execute(sql, list(data.values()))
        connection.commit()

    except Exception as e:
        print(e)
    finally:
        if connection:
            cur.close()
            connection.close()
            print("PostgreSQL connection is closed")
