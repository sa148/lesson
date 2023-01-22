# タイムゾーン設定 #
from datetime import datetime, timedelta, timezone
JST = timezone(timedelta(hours=+9))
result = datetime(2023, 1, 22, 1, 1, 1, tzinfo=JST)
print(result)
# 祝日か調べる #
import jpholiday 
from datetime import datetime

d = datetime(2023, 1, 22)
result = jpholiday.is_holiday(d)
print(result)

# 祝日全て #
import jpholiday

result = jpholiday.year_holidays(2023)
print(result)