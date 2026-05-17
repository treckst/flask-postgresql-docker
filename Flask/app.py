from flask import Flask, request, jsonify
from contextlib import contextmanager
import psycopg2
import pandas as pd

app = Flask(__name__)

@contextmanager
def auto_con():
    connection = psycopg2.connect(
        host='postgres_flask',
        database='flaskdb',
        user='postgres',
        password='postgres'
    )
    try:
        yield connection
    finally:
        connection.close()

@app.route('/', methods=['GET'])
def hello():
    
    return "Use /read to see the database\n/insert/<name> for data insertion\n/delete/<name> for data deletion"

@app.route('/read', methods=['GET'])
def read():
    
    with auto_con() as conn:
        df = pd.read_sql("SELECT id, name, to_char(loaded, 'YYYY-MM-DD HH24:MI:SS') AS loaded FROM users", conn)
    return df.to_json(), 200

#pandas doesn't work with sql_queries, so
@app.route('/insert/<name>', methods=['GET', 'POST'])
def insert(name):
    
    insert_query = "INSERT INTO users (name) VALUES (%s);"
    with auto_con() as conn:
        with conn.cursor() as cursor:
            cursor.execute(insert_query, (name,))
        conn.commit()
    return jsonify({'message': f'User {name} inserted successfully'}), 201


@app.route('/delete/<name>', methods=['GET', 'DELETE'])
def delete(name):

    delete_query = "DELETE FROM users WHERE name = %s;"
    with auto_con() as conn:
        with conn.cursor() as cursor:
            cursor.execute(delete_query, (name,))
        conn.commit()
    return jsonify({'message': f'User {name} deleted successfully'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)