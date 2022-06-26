from collections import deque


def solution(cards, shuffles):

    for i in range(len(shuffles)):
        size = len(cards) // 2
        if shuffles[i] == "Cut": # 리스트의 가운데 기준으로 위치를 바꾼다
            cards = cards[size:] + cards[:size]
        elif shuffles[i] == "Riffle": # 리스트의 가운데를 기준으로 두 리스트에서 하나씩 꺼내어 새 리스트 생성
            idx1 = size - 1
            idx2 = size * 2 - 1
            newCards = deque()
            while idx1 >= 0:
                newCards.appendleft(cards[idx1])
                newCards.appendleft(cards[idx2])
                idx1 -= 1
                idx2 -= 1
            cards = list(newCards)[:]
    return cards


print(solution([1,2,5,6,4,3], ["Cut", "Cut", "Cut"])) # [6, 4, 3, 1, 2, 5]
print(solution([5,2,4,6,3,1], ["Riffle", "Riffle", "Riffle"])) # [5, 2, 4, 6, 3, 1]
print(solution([2,3,6,5,4,1], ["Cut", "Riffle", "Cut"])) # [4, 6, 1, 2, 5, 3]