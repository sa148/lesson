# タプルとして受け取れる可変長引数 #
def func(*args, x):
    result = ','.join(args)
    print(f'{x}: {result}')

func('あ', x=1)
func('あ', 'A', 'a', x=2)