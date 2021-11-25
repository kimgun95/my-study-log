// 1103 - 게임
// DFS로 접근을 했다. 시도는 좋았으나 무한 반복이 될 수 있는 경우를 생각안했다. 즉 visited를 사용안했다.
// visited를 활용하여 한다해도 DFS로는 풀리지 않는 문제이다. 아마 해도 어려울듯.
// 따라서 DP를 함께 적용시켜야 하는 문제. 해당 좌표에서 최대로 움직일 수 있는 횟수를 저장하면 된다. 
#include <iostream>
using namespace std;

int N, M;
int arr[50][50]; // 지도 
bool visit[50][50]; // 방문 여부 
int DP[50][50]; // 최대 움직일 수 있는 횟수 저장. 
int dr[] = {-1, 1, 0, 0}, dc[] = {0, 0, -1, 1}; // 상하좌우 계산 용도. 

int ans = 0;


int DFS(int row, int col) {
	if (row < 0 || row >= N || col < 0 || col >= M || arr[row][col] == 0) return 0;
	// 이미 방문한 곳은 무한 순환이 가능하기 때문에 -1 출력 후 프로그램 종료. 
	if (visit[row][col] == true) {
		cout << -1 << endl;
		exit(0);
	}
	// DP가 -1이 아니라면 이전에 이미 갈 수 있는 최대경로를 계산한 상태이기 때문에 바로 반환. 
	if (DP[row][col] != -1) return DP[row][col];
	// DP를 0으로 세팅, 방문 체크를 한 후 DP값 시작. 
	visit[row][col] = true;
	DP[row][col] = 0;
	// 상하좌우 이동을 통해 DP값 계산. 
	for (int i = 0; i < 4; i++) {
		int row_num = row + (dr[i] * arr[row][col]);
		int col_num = col + (dc[i] * arr[row][col]);
		// 이동을 하는 것이니 +1 횟수 증가. 
		DP[row][col] = max(DP[row][col], DFS(row_num, col_num) + 1);
	}
	// 계산 끝났으니 방문 체크 초기화 
	visit[row][col] = false;
	return DP[row][col];
}

int main() {
	// 입력 받기. 
	cin >> N >> M;
    for (int i = 0; i < N; i++)
    {
        string s;
		cin >> s;
		// 입력 받은 string을 arr에 숫자형식으로 저장. 
        for (int j = 0; j < s.length(); j++)
        {
            if (s[j] == 'H') arr[i][j] = 0;
            else arr[i][j] = s[j] - '0';
        }
    }
    // DP를 -1로 모두 초기화. 
    for (int i = 0; i < N; i++) {
    	for (int j = 0; j < M; j++) {
    		DP[i][j] = -1;
		}
	}
    
    // DFS 시작. 
    ans = DFS(0,0); 
    
    cout << ans;

} 
