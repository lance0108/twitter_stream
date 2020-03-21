import psycopg2
from credentials import PG_CONN
import json
import pandas.io.sql as sqlio


def get_pg_connection():
    conn = psycopg2.connect(
        host=PG_CONN['host'],
        port=PG_CONN['port'],
        database=PG_CONN['db_name'],
        user=PG_CONN['user'],
        password=PG_CONN['password']
    )
    return conn


def validate_connection(conn):
    df1 = sqlio.read_sql_query("SELECT 1 AS one", conn)
    if df1["one"].iloc[0] == 1:
        return True
    return False


def insert_tweet(conn, table_name, tweet):
    cur = conn.cursor()
    q_insert = f"""
        INSERT INTO {table_name}
        (id, created_at, lang, raw_json)
        VALUES (%s, %s, %s, %s)
    """
    tweet_j = json.dumps(tweet)
    values = (
        tweet["id"],
        tweet["created_at"],
        tweet["lang"],
        tweet_j
    )
    cur.execute(q_insert, values)
    return True


