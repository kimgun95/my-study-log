def number_card_2():
    N = int(input())
    N_list = list(map(int, input().split()))
    M = int(input())
    M_list = list(map(int, input().split()))

    # N과 M의 자료의 크기가 500,000이 올 수도 있기 때문에 탐색시 hash를 이용하면 문제를 빠르게 해결할 수 있다.
    # dictionary는 hash를 이용한다.
    dic = {}
    for i in N_list:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    for i in M_list:
        if i in dic:
            print(dic[i], end='')
        else:
            print('0', end='')
        print(' ', end='')


number_card_2()