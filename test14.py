# 正常に作動 #
x = 1
y = 0

try:
    result = x / y
except ZeroDivisionError:
    print('ゼロで割ることはできません')