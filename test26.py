# タプル動作確認 #
x_tuple = (1, 2, 5)
y_list = (4, 5, 6)
y_tuple = tuple(y_list)

result = x_tuple[2]
print(result)

# タプル結合 #
x_tuple = (1, 3, 6)

y_list = [3, 4, 5]
y_tuple = tuple(y_list)

result = x_tuple + y_tuple
print(result)

# 戻り値複数 #
def test_function():
    x = 2 + 2
    y = 3 + 3
    return x, y

result1, result2 = test_function()
print(result1, result2)

# 戻り値変数１つ #
def test_function():
    x = 2 + 2
    y = 3 + 3
    return x, y

result1 = test_function()
print(result1)

# for文戻り値１つ #
x_dict = {'a' : 100, 'b' : 200, 'c' :300}
for x in x_dict.items():
    print(x)