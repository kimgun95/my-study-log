def main():
    test = int(input())
    for i in range(test):
        num = input().split(' ')
        N = int(num[0])
        K = int(num[1])

        mineral = [([]) for i in range(N)]
        for j in range(N):
            mineral[j] = list(map(int, input().split(' ')))

        # 미해결...ㅜ
main()