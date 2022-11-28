def solution(low, high, img):
    answer = 0
    height = len(img)
    width = len(img[0])


    def check_row(y,x,n):
        for i in range(n):
            if img[y][x+i] != '#' or img[y+n-1][x+i] != '#':
                return False
        return True


    def check_col(y,x,n):
        for i in range(n):
            if img[y+i][x] != '#' or img[y+i][x+n-1] != '#':
                return False
        return True


    def check_all(y,x,n):
        black = 0
        for i in range(1,n-1):
            for j in range(1,n-1):
                if img[y+i][x+j] == '#':
                    black += 1
        if low <= black * 100 / ((n-2)**2) < high:
            return True
        return False


    # 모든 정사각형을 탐색해야 할듯
    for i in range(height-2): # 모든 점에 대해
        for j in range(width-2):
            if img[i][j] == '#':
                n_max = min(height-i,width-j)
                for k in range(3,n_max+1): # 모든 가능한 정사각형에 대해
                    # 가로 외곽선 체크, 세로 외곽선 체크, 안에 내용을 체크
                    if check_row(i,j,k) and check_col(i,j,k) and check_all(i,j,k):
                        answer += 1

    return answer


print(solution(25,51,[".########......", ".####...#......", ".#.####.#.#####", ".#.#..#.#.#..##", ".#.##.#.#.#...#", ".#.####.#.#...#", ".#....###.#####", ".########......"]))
print(solution(25,50,[".########......", ".####...#......", ".#.####.#.#####", ".#.#..#.#.#..##", ".#.##.#.#.#...#", ".#.####.#.#...#", ".#....###.#####", ".########......"]))
print(solution(0,20,["#######....###..###.", "#.....#....#.#..#.#.", "#.....#....###..###.", "#.....#.............", "#..#########........", "#..#..#....#.....##.", "#######....#.....##.", "...#.......#........", "...#.......#........", "...#..##############", "...#..#....#.......#", "...#..#....#.......#", "...#########.......#", "......#............#", "......##############"]))