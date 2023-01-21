# 関数ミュータブル検証 #
def func(t):
    t = t + 999
    return t

x = 1
y = func(x)

print(x)
print(y)

# 関数ミュータブル検証 #
def func(t):
    t.append(999)
    return t

x = [1, 2, 3]
y = func(x)
print(x)
print(y)