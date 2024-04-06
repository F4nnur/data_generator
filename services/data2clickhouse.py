import clickhouse_connect


def insert_into_clickhouse(table_name: str, data: dict):
    try:
        client = clickhouse_connect.get_client(host='localhost', port=8123)
        keys = tuple(data.keys())
        keys_str = ', '.join(keys)
        vals = f'({keys_str})'
        query = f"""
        INSERT INTO {table_name}
        {vals}
        VALUES
        {tuple(data.values())}
        """
        client.query(query)

    except Exception as e:
        print(e)
