# 例外が発生しない処理 #
x = 3
y = 3

try:
    result = x / y
except ZeroDivisionError as e:
    print('ゼロで割れない')
    print(e)
except NameError as e:
    print('変数が定義されていません')
    print(e)
else:
  print(result)
  print('正常に処理されました')