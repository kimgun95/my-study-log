def solution(rooms, target):
    answer = []
    banned = set()
    picked = dict()
    min_dist = set()
    min_dist_val = float('inf')
    room = []

    for r in rooms:
        x = r.replace('[', '')
        x = x.replace(']', ',')
        x = x.split(',')
        x[0] = int(x[0])
        room.append(x)
    for ro in room: # 고려대상 제외
        if ro[0] == target:
            for member in ro[1:]:
                banned.add(member)
    for roo in room: # 지정자리 갯수 확인
        if roo[0] != target:
            for member in roo[1:]:
                if member not in picked:
                    picked[member] = 1
                else:
                    picked[member] += 1
    for i in room: # 최소 거리 계산
        if i[0] != target:
            value = abs(target - i[0])
            min_dist_val = min(min_dist_val, value)
    for i in room: # 최소 거리인 방 확인
        if i[0] != target:
            if abs(target - i[0]) == min_dist_val:
                min_dist.add(i[0])
    print(min_dist)
    return answer

solution(["[403]James", "[404]Azad,Louis,Andy", "[101]Azad,Guard"], 403)