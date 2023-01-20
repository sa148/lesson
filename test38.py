# lambda #
func = lambda x, y :print(f'{x}さんは{y}です')
func('佐々木', '学生')

# map関数 #
names = ['加藤', '斎藤', '後藤']
result = list(map(lambda x: x + 'さん', names))
print(result)

# 複数のリスト #
n1 = ['斎藤', '佐藤', '佐々木']
n2 = ['唯', '由衣', '結衣']
result = list(map(lambda x, y: x + y + 'さん', n1, n2))
print(result)

# fileter #
numbers = [5, 6, 7, 10, 15, 18]
result = list(filter(lambda x: x >= 10, numbers))
print(result)