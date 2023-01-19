# タイプアノテーション #
def total_price_1item(unit_price: int, quantity: int)-> int:
    total_price = unit_price * quantity
    return total_price

total_price = total_price_1item(130, 3)
print(total_price)

# 繰り返す #
def total_price_1item(unit_price: int, quantity: int)-> int:
    total_price = unit_price * quantity
    return total_price

total_price = total_price_1item(130, '1')
print(total_price)

# タイプアノテーション+デフォルト値 #
def total_price_1item(unit_price: int, quantity: int = 1)-> str:
    total_price = unit_price * quantity
    return f'{total_price:,}'

total_price = total_price_1item(1300)
print(total_price)