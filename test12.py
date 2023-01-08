def print_banana():
    # ここからが関数の処理部分 #
    print('banana')

print_banana()

# 下が引数使用 #
def print_text(text):
    # ここからが関数の処理部分 #
    print(text)

print_text('apple')

# 引数と戻り設定 #

def question_text(text):
    text_q = text + '?'
    return text_q

result_text = question_text('apple')
print(result_text)

# 複数の引数と戻り値 #
def qustion_exclamation_text(text1, text2):
    return_text1 = text1 + '?'
    return_text2 = text2 + '!'
    return return_text1, return_text2

r1, r2 = qustion_exclamation_text('apple', 'banana')
print(r1)
print(r2)