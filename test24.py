# writelinesリストデータ書き込み #
x_list = ['apple', 'orende', 'banana']
with open('test3.txt', 'w') as f:
    f.writelines(x_list)