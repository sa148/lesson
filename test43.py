# タイムゾーン設定 #
from datetime import datetime, timedelta, timezone
JST = timezone(timedelta(hours=+9))
result = datetime(2023, 1, 22, 1, 1, 1, tzinfo=JST)
print(result)