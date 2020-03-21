import json
import time
from datetime import datetime
from tweepy import Stream, StreamListener
from authentication import authenticate
from credentials import API_CREDENTIALS
from database import validate_connection, insert_tweet, get_pg_connection


def get_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


class PgListener(StreamListener):
    conn = None
    target_table = None
    coutner = None
    counter = 0

    def on_data(self, raw_data):
        tweet = json.loads(raw_data)
        insert_tweet(self.conn, self.target_table, tweet)
        self.counter += 1
        if self.counter % 100 == 0:
            self.conn.commit()
            print(
                get_time(),
                " | ",
                self.counter,
                flush=True
            )
        return True

    def on_error(self, status_code):
        print(status_code)

    def set_connection(self, conn_):
        self.conn = conn_
        validate_connection(self.conn)

    def set_target_table(self, table_name):
        self.target_table = table_name

    def reset_counter(self):
        self.counter = 0


def start_streaming(
    credential,
    target_table,
    tracks=None,
    locations=None
):
    assert (tracks is not None) or (locations is not None)
    listener = PgListener()
    listener.reset_counter()
    listener.set_target_table(target_table)
    listener.set_connection(get_pg_connection())
    auth = authenticate(credential)
    stream = Stream(auth, listener)
    if tracks is not None:
        stream.filter(track=tracks)
    elif locations is not None:
        stream.filter(locations=locations)


if __name__ == "__main__":
    credential = API_CREDENTIALS[1298440]
    target_table = "twitter.nyc"
    tracks = ["NYC", "New York"]
    while True:
        try:
            print(get_time(), " | ", "Reset")
            start_streaming(credential, target_table, tracks)
        except Exception as e:
            print(get_time(), " | ", "Exception!")
            print(e)
            time.sleep(60)
