seat_count = 9
vip_seat_array = [4, 7]

fibonacci_memo = {
    1: 1,
    2: 2
}


def get_all_ways_of_theater_seat(total_count, fixed_seat_array):
    count_of_case = 1
    count_seat = 0
    for num in range(1, total_count + 2):
        if (num in fixed_seat_array) or (num == total_count + 1):
            count_of_case *= fibonacci(count_seat, fibonacci_memo)
            count_seat = 0
        else:
            count_seat += 1
    return count_of_case


def fibonacci(number, memo):
    if number in memo:
        return memo[number]
    nth_fibo = fibonacci(number - 1, fibonacci_memo) + fibonacci(number - 2, fibonacci_memo)
    fibonacci_memo[number] = nth_fibo
    return nth_fibo


# 12가 출력되어야 합니다!
print(get_all_ways_of_theater_seat(seat_count, vip_seat_array))
