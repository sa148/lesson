# 集合x_Set #
x_set = {11, 222, 333}

y_list = [11, 222, 444, 555, 11]
y_set = set(y_list)

print(x_set)
print(y_set)

# 積集合を取得 #
x_set = {11, 222, 333}

y_list = [11, 222, 444, 555, 11]
y_set = set(y_list)

result = x_set & y_set
print(result)

# 差集合 #
x_set = {11, 222, 333}

y_list = [11, 222, 444, 555, 11]
y_set = set(y_list)

result = x_set - y_set
print(result)

