import json
import time
import pandas as pd
from datetime import datetime

from pymongo import MongoClient
from tweepy import Stream, StreamListener
from authentication import authenticate
from credentials import API_CREDENTIALS, MG_CONN


def get_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


class MongodListener(StreamListener):

    def __init__(self, coll):
        super().__init__()
        self.counter = 0
        self.target_coll = coll

    def on_data(self, raw_data):
        tweet = json.loads(raw_data)
        if not "created_at" in tweet.keys():
            print(tweet)
            return False
        tweet["created_at"] = pd.to_datetime(tweet["created_at"])
        try:
            self.target_coll.insert_one(tweet)
            self.counter += 1
        except Exception as ex:
            print(ex)

        if self.counter % 100 == 0:
            print(
                get_time(),
                " | ",
                self.counter,
                flush=True
            )
        return True

    def on_error(self, status_code):
        print(status_code)
        if status_code == 420:
            # returning False in on_data disconnects the stream
            return False
            # should I raise an exception here?


def start_streaming(
        credential,
        target_db,
        target_coll,
        tracks=None,
        locations=None
):
    assert (tracks is not None) or (locations is not None)
    client = MongoClient(MG_CONN["URL"])
    coll = client[target_db][target_coll]
    listener = MongodListener(coll)
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
