import mysql.connector as connector
from mysql.connector import Error

def Connect(host, database, user, password, auth_plugin='mysql_native_password'):
    try:
        conn = connector.connect(
            host = host,
            database = database,
            user = user,
            password = password,
            auth_plugin = auth_plugin)
        if conn.is_connected():
            print('Connected to MySQL database "{}"'.format(database))
    except Error as e:
        print(e)
    return conn

def Disconnect(conn):
    if conn is not None and conn.is_connected(): 
        conn.close()
        print('Connection closed')

def Insert(conn, original, shortened):
    sql = """INSERT INTO links (original, shortened) 
             VALUES (%s, %s)"""
    cursor = conn.cursor()
    cursor.execute(sql, (original, shortened))
    try:
        conn.commit()
    except Error as e:
        print(e)
    finally:
        if(conn):
            cursor.close()

def Select(conn, shortened):
    sql = "SELECT * FROM links WHERE shortened = %s"
    cursor = conn.cursor(buffered=True)
    cursor.execute(sql, (shortened,))
    results = cursor.fetchall()
    if(conn):
        cursor.close()
    return results

# Some usage examples:
# conn = Connect('localhost', 'url_shortener', 'admin', input('Please, input password: '))
# Insert(conn, 'testing1', 'whatever link')
# selection = Select(conn, 'some link')
# for s in selection:
#    print(s)
# Disconnect(conn)
