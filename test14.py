# 正常に作動 #
x = 1
y = 0

try:
    result = x / y
except ZeroDivisionError:
    print('ゼロで割ることはできません')

# 例外オブジェクトを変数に代入 #
x = 1
y = 0

try:
    result = x / y
except ZeroDivisionError as e:
    print('ゼロで割ることはできません')
    print(e)

