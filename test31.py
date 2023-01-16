# 奇数だけのリスト #
x = [i for i in range(11) if i % 2 != 0]
print(x)

# aが入っている物を取得 #
foods = ['apple', 'banana', 'lemon']
x = [i for i in foods if 'a' in i]
print(x)