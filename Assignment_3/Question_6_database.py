from **** import ****
import sqlite3

DB_FILE = ''


def connect():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn

def close(conn):
   conn.close()


def get_data(conn, region, date):
    play = conn.cursor()
    query = f"SELECT * FROM **** WHERE **** = {region} AND **** = {date}"
    play.execute(query)
    result = play.fetchall()
    return result
