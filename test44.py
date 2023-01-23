# 可変長引数 #
def func(*args):
    print(args)

func(1)
func(1, 3, 10)

# 可変長引数文字あり #
def func(*args):
    result = ',' .join(args)
    print(result)

func('あ')
func('あ', 'A', 'a')