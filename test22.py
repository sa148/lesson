# 先頭２行のみ読み込み #
with open('test.text') as f:
    for _ in range(2):
      s_line = f.readline
      print(s_line)