# 現在の日付時刻 #
from datetime import datetime
n = datetime.now()
print(n)

# 日付の計算 #
from datetime import datetime, timedelta
d1 = datetime(2023, 1, 1)
d2 = datetime(2023, 1, 22)
result = d1 - d2
print(result)
print(result.days)

# 日付進めた #
from datetime import datetime, timedelta
d = datetime(2022, 12, 31, 1, 0, 0)
result = d + timedelta(days=10)
print(result)