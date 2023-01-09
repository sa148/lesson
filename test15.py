# finallyを追加 #
x = 2
y = 0

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
finally:
    print('割り算を修了します')