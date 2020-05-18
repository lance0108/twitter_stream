import time
from credentials import API_CREDENTIALS
from streaming_mg import get_time, start_streaming

if __name__ == "__main__":
    credential = API_CREDENTIALS[1583015]
    tracks = [
        "reopen",
        "re-open",
        "reopens",
        "re-opens",
        "reopening",
        "re-opening",
        "lockdown",  # will match 'lock-down' and 'lock down'
        "vaccine"
    ]
    while True:
        try:
            print(get_time(), " | ", "Reset")
            start_streaming(
                credential,
                target_db="corona",
                target_coll="reopen",
                tracks=tracks
            )
        except Exception as e:
            print(get_time(), " | ", "Exception!")
            print(e)
            time.sleep(60)
