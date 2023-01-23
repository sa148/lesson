# タプルとして受け取れる可変長引数 #
def func(*args, x):
    result = ','.join(args)
    print(f'{x}: {result}')

func('あ', x=1)
func('あ', 'A', 'a', x=2)

# 辞書で受け取る可変長引数 #
def func(**kwargs):
    print(kwargs)

func(name='斎藤', user_id=222)
func(item='牛乳', item_id=111, price=100)
