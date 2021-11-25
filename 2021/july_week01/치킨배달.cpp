// 15686 - ġŲ���.
// �̹��� SDS �˰��� ���� Ǯ�鼭 ó������ 99% ���� § �ڵ�.
// �ð� �ʰ��� �߻��ؼ� �ٸ� �� �ڵ带 ���� �Ǿ��µ� dfs�� depth�� �ִ°� �ƴ϶�
// idx���� �־��־ �� �� Ž���� �� �ϰ� ���־���. �ʹ� �ƽ��� �� ����
 
#include <iostream>
#include <vector>
#include <algorithm> // abs ���. 
using namespace std;

typedef pair<int, int> pii;

int N, M;
int arr[50][50]; // map�� �Է� �޴� ��. 
int ans  = 2000000000; // ����� ��� ����. 
vector<pii> home_loc; // ��� �������� ��ǥ
vector<pii> chicken_loc; // ��� ġŲ���� ��ǥ 
bool chicken_check[13] = {false,}; // vector�� ������ ġŲ���� ���� ���Ǹ� �湮�� �� ������ üũ. 
vector<pii> visit; // ����� ġŲ�� ��ǥ 

// �������� ġŲ������ �ּ� �Ÿ� ���. 
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

// ġŲ���� dfs�� ���� �� Ž��. 
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
	// �Է� �ޱ�. 
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
