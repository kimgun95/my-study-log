//n = int(input())
//# n크기 만큼 배열 초기화
//q = [0 for i in range(n)]
//cnt = 0
//
//# 가지치기 함수(유망하지 않은 노드들은 탐색하지 않으며 유망한 노드에 대해서만 탐색을 한다)
//def pruning(q, n):
//    # 이전에 놓았던 퀸들과 동선이 겹치는지 확인
//    for i in range(n):
//        # 같은 열에 있다면 false
//        if q[i] == q[n]:
//            return 0
//        #  오른쪽 위 방향에 퀸이 있다면 false
//        if (q[i] - q[n]) == (n - i):
//            return 0
//        #  왼쪽 위 방향에 퀸이 있다면 false
//        if (q[n] - q[i]) == (n - i):
//            return 0
//    return 1
//
//# 0번째 배열부터 퀸을 하나씩 추가한다
//# n은 0이 첫 시작이고 n + 1을 통해 늘려간다
//def nQueen(q, n):
//    length = len(q)
//    # 퀸을 끝까지 채우는데 성공하면 cnt를 증가시킨다
//    if n == length:
//        global cnt
//        cnt += 1
//    else:
//        # n번째 배열에 i위치에 퀸을 놓는다
//        for i in range(length):
//            q[n] = i
//            # 가지치기를 실시하며 유망한 노드 발견시 다음 배열에 퀸 배치를 시작한다
//            if pruning(q, n) == 1:
//                nQueen(q, n+1)
//
//nQueen(q, 0)
//print(cnt)

#include <iostream>
using namespace std;

int main() {
	return 0;
}
