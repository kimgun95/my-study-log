# 1476 - 날짜계산
# 1 ≤ E ≤ 15, 1 ≤ S ≤ 28, 1 ≤ M ≤ 19
def main():
    a, b, c = map(int, input().split())
    cnt = 1
    E = 1
    S = 1
    M = 1
    while True:
        if E == a and S == b and M == c:
            print(cnt)
            break
        E = E + 1
        S = S + 1
        M = M + 1
        if E >= 16:
            E = 1
        if S >= 29:
            S = 1
        if M >= 20:
            M = 1
        cnt = cnt + 1


main()