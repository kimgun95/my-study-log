shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "사이다"]


def is_available_to_order(menus, orders):
    for i in orders:
        if i not in menus:
            return False
    return True
#     sorted_menus = sorted(menus)
#     for i in orders:
#         if binary_search_in_menus(sorted_menus, i) is False:
#             return False
#     return True
#
# def binary_search_in_menus(menus, order):
#     min_idx = 0
#     max_idx = len(menus) - 1
#     guess = (min_idx + max_idx) // 2
#
#     while min_idx <= max_idx:
#         if order == menus[guess]:
#             return True
#         elif order <= menus[guess]:
#             max_idx = guess - 1
#         else:
#             min_idx = guess + 1
#         guess = (min_idx + max_idx) // 2
#     return False


result = is_available_to_order(shop_menus, shop_orders)
print(result)