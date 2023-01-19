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
