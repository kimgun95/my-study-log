shop_prices = [3000, 20000, 1500]
user_coupons = [20, 40, 10, 30, 70]


def get_max_discounted_price(prices, coupons):
    price_total = 0
    prices.sort()
    coupons.sort()
    while len(prices) > 0 and len(coupons) > 0:
        price = prices.pop()
        discount = coupons.pop()
        price_total += price * (100 - discount) // 100
    if len(prices) != 0:
        while len(prices):
            price_total += prices.pop()

    return price_total


print(get_max_discounted_price(shop_prices, user_coupons))  # 8850 이 나와야 합니다.
