import time

from credentials import API_CREDENTIALS
from steaming import get_time, start_streaming

if __name__ == "__main__":
    credential = API_CREDENTIALS[1582449]
    target_table = "twitter.nyc"
    locations = [-74.2591, 40.4774, -73.7002, 40.9162]
    while True:
        try:
            print(get_time(), " | ", "Reset")
            start_streaming(
                credential,
                target_table,
                locations=locations
            )
        except Exception as e:
            print(get_time(), " | ", "Exception!")
            print(e)
            time.sleep(60)
