# ゼロ埋め #
x = 123
result = f'No: {x:010}'
print(result)

# 金額用カンマ #
x = 9000000
result = f'{x:,}円です'
print(result)

# 小数点以下の桁数 #
x = 0.123
result = f'{x:.5f}'
print(result)