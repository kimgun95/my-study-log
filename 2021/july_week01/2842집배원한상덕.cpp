// 2842 - ������ѻ��
// dfs�������� ��ǥ�̵��� �� �� �ִ� ���� �̵��ϸ鼭 ����� �ߴ�. ���ó� �ð� �ʰ��� �߻��ߴ�. 
// �ذ���� �������� �˰����̾���. �ϴ� ���̵�� ���� �Ź��ϴ�. ���� ���Ϳ� ���Ľ�Ų �� �ߺ� ���� ���Ÿ� �Ѵ�.
// �������ͷ� left, right�� 0, 0�������� left < x < right �� ������ �� �� �ִ� ��θ� Ž���ϸ� right - left�� �ּڰ��� ã�� ���̴�.
// �Ӹ��� �ʹ� �ȱ�������. ���� ���� ���� ��α׸� 3��°�� �߰��ؼ� ������ߴ�. se...ba.... 
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <memory.h>
using namespace std;

typedef pair<int, int> pii;

int N;
char name[50][50]; // P, K �Է� �޴� �迭. 
int alti[50][50]; // �� �Է� �޴� �迭. 
int K = 0; // K�� ���� 
vector<int> alti_sort; // �� ���� �� �ߺ� �� ������ ����. 

bool visit[50][50]; // �湮����. 
pii location;
// ��, ���, ��, ����, ��, ����, ��, �»� �̵� 
int dy[8] = {-1, -1, 0, 1, 1, 1, 0, -1};
int dx[8] = {0, 1, 1, 1, 0, -1, -1, -1};

int ans = 1000000; // ���� ���. 

// �� ���� left, right�� �޾� ��. 
bool bfs(int l, int r) {
	// ť�� ���� ��ġ �־��ְ� �湮 üũ. 
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
			// ��ǥ �̵����Ѻ� �� ��ȿ�� ��ǥ���� üũ. 
			int ny = y + dy[i];
			int nx = x + dx[i];
			if (nx < 0 || nx >= N || ny < 0 || ny >= N || visit[ny][nx]) continue;
			if (alti[ny][nx] < l || alti[ny][nx] > r) continue;
			
			// ��ȿ�ϴٸ� �湮üũ �� ť�� �߰�. 
			visit[ny][nx] = true;
			q.push({ny, nx});
		}
	}
	return false;
}

int main() {
	// �Է� �ޱ�. 
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
	// �켱 ���� ���� �� �ߺ��� ���� unique, erase �Լ��� �����Ѵ�.
	// unique�� �ߺ��� ������ �ڷ� �Ѱ��ָ� ��ȯ�� �ߺ��� ������ �� ó���� ��ȯ�Ѵ�. 
	// erase�� �ش� ������ ������ �������ش�. 
	sort(alti_sort.begin(), alti_sort.end());
	alti_sort.erase(unique(alti_sort.begin(), alti_sort.end()), alti_sort.end());
	
	
	int left = 0, right = 0; // �� ������ ���� �̿�. 
	
	while (right < alti_sort.size()) {
		while (1) {
			bool possible = false;
			// Ž���ϰ� �ִ� �� �������� ��Ҷ�� Ž���� �Ѵ�. 
			if (alti_sort[left] <= alti[location.first][location.second] &&
			alti[location.first][location.second] <= alti_sort[right]) {
				possible = bfs(alti_sort[left], alti_sort[right]);
				memset(visit, 0, sizeof(visit));
			}
				
			if (possible == false) break;
			// Ž���� ���������� ���´ٸ� �� ���̸� ����ϸ� ans���� �ּڰ� �񱳸� �Ѵ�. 
			int diff = alti_sort[right] - alti_sort[left];
			if (ans > diff) ans = diff;
			// Ž�� ����� true�̴� left++�� ���� Ž���� �õ��غ���. 
			left++;
		}
		// left++�δ� �ȵǰų� ��ư �ȵǸ� right++�� ������ �ø���. 
		right++;
	} 
	
	cout << ans;
	
	
	return 0;
} 
