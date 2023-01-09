# 例外オブジェクトを複数 #

x = 2

try: 
    result = x / y
except ZeroDivisionError as e:
    print('ゼロで割ることはできません')
    print(e)
except NameError as e:
    print('変数が定義されていません')
    print(e)
