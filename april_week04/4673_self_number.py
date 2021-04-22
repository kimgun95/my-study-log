def self_number(number):
    num = number
    total = number
    while num // 10:
        total += num % 10
        num = num // 10
    total += num % 10
    return total


def solution():
    list = []
    for i in range(1, 10001):
        number = i
        while True:
            num = self_number(number)

            if num not in list and num <= 10000:
                list.append(num)
            else:
                break
            number = num
    for i in range(1, 10001):
        if i not in list:
            print(i)


solution()