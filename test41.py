# 今日の日付の取得 #
from datetime import date
t = date.today()
print(t)

# 日付で取得 #
from datetime import date
d = date(2022, 1, 22)
print(d)

# 曜日取得 #
from datetime import date
d = date(2022, 1, 22)
print(d)
print(d.weekday())