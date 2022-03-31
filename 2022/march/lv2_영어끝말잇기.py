def solution(n, words):
    s = set()
    s.add(words[0])
    before_word = words[0]
    turn = 0
    for idx in range(1, len(words)):
        turn += 1
        if (words[idx] in s) or (before_word[-1] != words[idx][0]):
            return [(turn % n) + 1, (turn // n) + 1]
        before_word = words[idx]
        s.add(before_word)
    return [0, 0]


print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))