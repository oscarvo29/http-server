from datetime import datetime
import zoneinfo
import time


def get_formatted_time() -> str:
    now = "Date: "
    time_struct = time.localtime()
    tz = zoneinfo.ZoneInfo("Europe/Copenhagen")
    timezone = datetime.now(tz).tzname()

    now = now + time.strftime("%a, %d %b %Y %H:%M:%S", time_struct) 
    now = now + " " + timezone

    return now