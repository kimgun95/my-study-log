def main():
    num = int(input())
    dic = []
    for i in range(num):
        dic.append(input())
    # 공백 입력
    input().strip()

    board = int(input())
    for i in range(board):
        ex = []
        for j in range(4):
            ex.append(input())
        # 답안 처리

        print(ex)
        if i != board - 1:
            input().strip()




main()