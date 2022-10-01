def solution(registered_list, new_id):
    dict = {}
    for rl in registered_list:
        dict[rl] = True
    i = 0
    size = len(new_id)
    while new_id[i]:
        i += 1
        if i > size-1 or not 'a' <= new_id[i] <= 'z':
            break

    front, back = new_id[:i], -1
    if new_id[i:] == '':
        back = 0
    else:
        back = int(new_id[i:])

    if new_id not in dict:
        return new_id
    while True:
        back += 1
        if front + str(back) not in dict:
            return front + str(back)


print(solution(["card", "ace13", "ace16", "banker", "ace17", "ace14"], "ace15"))
print(solution(["cow", "cow1", "cow2", "cow3", "cow4", "cow9", "cow8", "cow7", "cow6", "cow5"], "cow"))
print(solution(["bird99", "bird98", "bird101", "gotoxy"], "bird98"))
print(solution(["apple1", "orange", "banana3"], "apple"))