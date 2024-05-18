import datetime
import time

def countdown_timer():
    now = datetime.datetime.now()
    end_date = datetime.datetime(2024,12,31)
    remaining_time = end_date - now
    while True:
        if remaining_time.total_seconds() > 0:
            print("Time remaining", remaining_time)
            time.sleep(1)
        else:
            print("Time's up!")

countdown_timer()
