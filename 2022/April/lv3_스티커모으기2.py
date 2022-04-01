def solution(sticker):
    length = len(sticker)
    if length <= 3: # 3개 이하일 때 바로 답 리턴
        return max(sticker)
    # 처음 찢고 시작(마지막 찢기 불가능)
    dp1 = [0] * length
    dp1[0], dp1[2] = sticker[0], sticker[0] + sticker[2]
    idx = 3
    while 3 <= idx < length:
        dp1[idx] = max(dp1[idx - 2], dp1[idx - 3]) + sticker[idx]
        idx += 1
    # 처음 안찢고 시작(마지막 찢기 가능)
    dp2 = [0] * length
    dp2[1], dp2[2] = sticker[1], sticker[2]
    idx = 3
    while 3 <= idx < length:
        dp2[idx] = max(dp2[idx - 2], dp2[idx - 3]) + sticker[idx]
        idx += 1
    max1 = max(dp1[:length - 1]) # 마지막 찢기 불가능
    max2 = max(dp2[:length]) # 마지막 찢기 가능
    return max(max1, max2)


print(solution([14, 6, 5, 11, 3, 9, 2, 10]))
print(solution([1, 3, 2, 5, 4]))