import heapq
# 라면의 남은 량
ramen_stock = 10
# 해외 공급업체에서 공급 가능 날짜
supply_dates = [4, 10, 15]
# 공급 날짜에 공급 되는 라면 량
supply_supplies = [11, 19, 5]
# 기존 공급업체에서 공급 회복이 되는 날짜
supply_recover_k = 30


# 내가 한 가지 막혔던 점
# 아래 for문을 진행하면서 공급량을 heap에 저장을 하고 나중에 최대값을 꺼내어 사용하는 데
# 이를 다음에 초기화하지 않고 그대로 또 다음 날짜부터 push를 통해 저장하면 또 pop을 할 때 이미 지나간 날의 공급량을 꺼낼 수도 있는거 아닌가?
# 라고 생각을 했다. 근데 그 논리는 맞는 논리이다.
# 사실 실제로 시간이 흘러 공급 받은 게 아니고 최적의 공급량을 지금 계산을 해내는 것이기 때문에 지나간 날이라도 최대값이라면 일정에 추가 후
# 실세계에서 해당 최적의 날짜에 공급을 받으면 된다.
def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):
    day_count = 0
    current_day = 0
    max_heap = []
    # stock을 k이상의 값이 될 때 까지 반복
    while stock < k:
        for date_index in range(current_day, len(dates)):
            # 날짜가 stock의 양보다 크면 안됨
            if dates[date_index] <= stock:
                heapq.heappush(max_heap, supplies[date_index] * -1)
            # 큰 날짜를 만나면 다음 for문을 위해 current_day에 날짜를 저장 후 break
            else:
                current_day = date_index
                break
        # max_heap에서 최댓값을 stock에 플러스
        stock += heapq.heappop(max_heap) * -1
        day_count += 1

    return day_count


print(get_minimum_count_of_overseas_supply(ramen_stock, supply_dates, supply_supplies, supply_recover_k))

