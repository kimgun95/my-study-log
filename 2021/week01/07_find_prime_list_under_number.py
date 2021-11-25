input_val = 100


# number가 소수인지 판단
def is_prime(number):
    if number == 1:
        return False
    elif number == 2:
        return True
    else:
        for i in range(2, number):
            if number % i == 0:
                return False
    return True


# numer의 소수들을 리스트로 반환
def find_prime_list_under_number(number):
    prime_num = []
    for i in range(1, number):
        if is_prime(i):
            prime_num.append(i)
    return prime_num


result = find_prime_list_under_number(input_val)
print(result)
