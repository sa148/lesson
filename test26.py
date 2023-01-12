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
