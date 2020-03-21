import time

from credentials import API_CREDENTIALS
from streaming import get_time, start_streaming

if __name__ == "__main__":
    credential = API_CREDENTIALS[2817015]
    target_table = "twitter.corona"
    tracks = [
        "coronavirus",
        "covid_19",
        "covid-19",
        "covid19",
        # "CoronaVirusUpdate",
        # "cdc",
        # "CoronavirusOutbreak"
    ]
    while True:
        try:
            print(get_time(), " | ", "Reset")
            start_streaming(
                credential,
                target_table,
                tracks=tracks
            )
        except Exception as e:
            print(get_time(), " | ", "Exception!")
            print(e)
            time.sleep(60)
