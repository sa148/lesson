# 書き込み #
with open('test2.txt', 'w') as f:
    f.write('あああ\nいいい')

# 追記 #
with open('test.txt', 'a') as f:
    f.write('\nえええ\nおおお')