# exception使用 #
x = 5

try:
    result = x / y
except Exception as e:
    print('例外が発生しました')
    print(e)