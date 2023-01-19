# リスト内包表記 #
x = [i for i in range(6)]
print(x)

# 名前版 #
names = ['斎藤', '山田', '田中']
x = [i + 'さん' for i in names]
print(x)

# 条件付き #
x = [i for i in range(11) if i % 2 != 0]
print(x)

# リスト #
foods = ['apple', 'banana', 'lemon']
x = [i for i in foods if 'a' in i]
print(x)