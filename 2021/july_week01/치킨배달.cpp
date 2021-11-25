// 15686 - 치킨배달.
// 이번에 SDS 알고리즘 문제 풀면서 처음으로 99% 내가 짠 코드.
// 시간 초과가 발생해서 다른 분 코드를 보게 되었는데 dfs에 depth만 넣는게 아니라
// idx값도 넣어주어서 좀 더 탐색을 덜 하게 해주었다. 너무 아쉽네 ㅠ ㅎㅎ
 
#include <iostream>
#include <vector>
#include <algorithm> // abs 사용. 
using namespace std;

typedef pair<int, int> pii;

int N, M;
int arr[50][50]; // map을 입력 받는 곳. 
int ans  = 2000000000; // 출력할 결과 저장. 
vector<pii> home_loc; // 모든 가정집의 좌표
vector<pii> chicken_loc; // 모든 치킨집의 좌표 
bool chicken_check[13] = {false,}; // vector에 저장한 치킨집과 같이 사용되며 방문을 한 곳인지 체크. 
vector<pii> visit; // 살려둘 치킨집 좌표 

// 가정집과 치킨집과의 최소 거리 계산. 
void route() {
	int res = 0;
	for (int i = 0; i < home_loc.size(); i++) {
		int min_dis = 2000000000;
		for (int j = 0; j < visit.size(); j++) {
			int cal = 0;
			cal = abs(home_loc[i].first - visit[j].first) + 
				abs(home_loc[i].second - visit[j].second);
			min_dis = min(min_dis, cal);
		}
		res += min_dis;
	}
	ans = min(ans, res);
	return;
}

// 치킨집을 dfs로 선택 및 탐색. 
void dfs(int depth, int idx) {
	if (depth == M) {
		route();
		return;
	}
	for (int i = idx; i < chicken_loc.size(); i++) {
		if (chicken_check[i]) continue;
		chicken_check[i] = true;
		visit.push_back(chicken_loc[i]);
		dfs(depth + 1, i);
		chicken_check[i] = false;
		visit.pop_back();
	}
	return;
}


int main() {
	// 입력 받기. 
	cin >> N >> M;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cin >> arr[i][j];
			if (arr[i][j] == 2) {
				chicken_loc.push_back(pii(i, j));
			} else if (arr[i][j] == 1) {
				home_loc.push_back(pii(i, j));
			}
		}
	}
	dfs(0, 0);
	cout << ans;
	return 0;
}
