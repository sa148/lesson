# lambda #
func = lambda x, y :print(f'{x}さんは{y}です')
func('佐々木', '学生')

# map関数 #
names = ['加藤', '斎藤', '後藤']
result = list(map(lambda x: x + 'さん', names))
print(result)

