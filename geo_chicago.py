import time

from credentials import API_CREDENTIALS
from streaming_mg import get_time, start_streaming

if __name__ == "__main__":
    credential = API_CREDENTIALS[1582428]
    target_db = "spothero"
    target_coll = "geo_chicago"
    # bbox = ["-87.968437,41.624851", "-87.397217,42.07436"]
    locations = [-87.968437, 41.624851, -87.397217, 42.07436]
    while True:
        try:
            print(get_time(), " | ", "Reset")
            start_streaming(
                credential,
                target_db,
                target_coll,
                locations=locations
            )
        except Exception as e:
            print(get_time(), " | ", "Exception!")
            print(e)
            time.sleep(60)
