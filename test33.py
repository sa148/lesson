# タイプアノテーション（デフォルト値なし）#
def total_price_1item(unit_price, quantity):
    total_price = unit_price * quantity
    return total_price

total_price = total_price_1item(120)
print(total_price)

# デフォルト値あり #
def total_price_1item(unit_price, quantity = 1):
    total_price = unit_price * quantity
    return total_price

total_price = total_price_1item(120)
print(total_price)

# 関数の呼び出し側で引数名前を指定して値を指定 #
def total_price_1item(unit_price, quantity = 1):
    total_price = unit_price * quantity
    return total_price

total_price = total_price_1item(quantity=20, unit_price=130)
print(total_price)
