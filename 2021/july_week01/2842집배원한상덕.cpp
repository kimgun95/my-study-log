// 2842 - 집배원한상덕
// dfs느낌으로 좌표이동을 할 수 있는 곳은 이동하면서 계산을 했다. 역시나 시간 초과가 발생했다. 
// 해결법은 투포인터 알고리즘이었다. 일단 아이디어 부터 신박하다. 고도를 벡터에 정렬시킨 후 중복 고도는 제거를 한다.
// 투포인터로 left, right를 0, 0시작으로 left < x < right 내 고도에서 갈 수 있는 경로를 탐색하며 right - left의 최솟값을 찾는 것이다.
// 머리가 너무 안굴러간다. 하필 설명 잘한 블로그를 3번째에 발견해서 개고생했다. se...ba.... 
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <memory.h>
using namespace std;

typedef pair<int, int> pii;

int N;
char name[50][50]; // P, K 입력 받는 배열. 
int alti[50][50]; // 고도 입력 받는 배열. 
int K = 0; // K의 갯수 
vector<int> alti_sort; // 고도 정렬 후 중복 고도 제거한 벡터. 

bool visit[50][50]; // 방문여부. 
pii location;
// 상, 우상, 우, 우하, 하, 좌하, 좌, 좌상 이동 
int dy[8] = {-1, -1, 0, 1, 1, 1, 0, -1};
int dx[8] = {0, 1, 1, 1, 0, -1, -1, -1};

int ans = 1000000; // 정답 출력. 

// 고도 범위 left, right를 받아 옴. 
bool bfs(int l, int r) {
	// 큐에 현재 위치 넣어주고 방문 체크. 
	queue<pii> q;
	q.push({location.first, location.second});
	visit[location.first][location.second] = true;
	int temp = 0;
	
	while (q.empty() == 0) {
		int y = q.front().first;
		int x = q.front().second;
		
		q.pop();
		if (name[y][x] == 'K') {
			temp++;
			if (temp == K) return true;
		}
		
		for (int i = 0; i < 8; i++) {
			// 좌표 이동시켜본 뒤 유효한 좌표인지 체크. 
			int ny = y + dy[i];
			int nx = x + dx[i];
			if (nx < 0 || nx >= N || ny < 0 || ny >= N || visit[ny][nx]) continue;
			if (alti[ny][nx] < l || alti[ny][nx] > r) continue;
			
			// 유효하다면 방문체크 및 큐에 추가. 
			visit[ny][nx] = true;
			q.push({ny, nx});
		}
	}
	return false;
}

int main() {
	// 입력 받기. 
	cin >> N;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cin >> name[i][j];
			if (name[i][j] == 'K') K++;
			if (name[i][j] == 'P') {
				location.first = i;
				location.second = j;
			}
		}
	}
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cin >> alti[i][j];
			alti_sort.push_back(alti[i][j]);
		}
	}
	// 우선 고도를 정렬 후 중복된 값은 unique, erase 함수로 삭제한다.
	// unique는 중복된 값들은 뒤로 넘겨주며 반환은 중복된 값들의 맨 처음을 반환한다. 
	// erase는 해당 범위의 값들을 삭제해준다. 
	sort(alti_sort.begin(), alti_sort.end());
	alti_sort.erase(unique(alti_sort.begin(), alti_sort.end()), alti_sort.end());
	
	
	int left = 0, right = 0; // 투 포인터 개념 이용. 
	
	while (right < alti_sort.size()) {
		while (1) {
			bool possible = false;
			// 탐색하고 있는 고도 범위내의 장소라면 탐색을 한다. 
			if (alti_sort[left] <= alti[location.first][location.second] &&
			alti[location.first][location.second] <= alti_sort[right]) {
				possible = bfs(alti_sort[left], alti_sort[right]);
				memset(visit, 0, sizeof(visit));
			}
				
			if (possible == false) break;
			// 탐색을 성공적으로 끝냈다면 고도 차이를 계산하며 ans와의 최솟값 비교를 한다. 
			int diff = alti_sort[right] - alti_sort[left];
			if (ans > diff) ans = diff;
			// 탐색 결과가 true이니 left++을 통해 탐색을 시도해본다. 
			left++;
		}
		// left++로는 안되거나 무튼 안되면 right++로 범위를 늘린다. 
		right++;
	} 
	
	cout << ans;
	
	
	return 0;
} 
