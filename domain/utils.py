
import datetime

def get_datetime_as_jst():
    return datetime.datetime.now(
    datetime.timezone(datetime.timedelta(hours=9))
)