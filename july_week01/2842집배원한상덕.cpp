#include <iostream>
using namespace std;

typedef pair<int, int> pii;

int N;
char name[50][50];
int alti[50][50];
int K = 0;
int low, high;
bool visit[50][50] = {false,};
int ans = 1000000;

bood valid(int x, int y) {
	if (x < 0 || y < 0 || x >= N || y >= N) return false;
	if (visit[x][y] == true) return false;
	return true;
}
void go(int x, int y, int depth) {
	if (depth == K) {
		ans = min(ans, high - low);
		return;
	}
	
	if (valid(x, y) == false) return;
	
	int dep = depth;
	if (name[x][y] == 'K') dep += 1;
	
	visit[x][y] = true;
	low = min 
	// 좌상 이동.
	go(x - 1, y - 1, dep);
	// 상 이동.
	go(x - 1, y, dep);
	// 우상 이동.
	go(x - 1, y + 1, dep);
	// 좌 이동.
	go(x, y - 1, dep);
	// 우 이동.
	go(x, y + 1, dep);
	// 좌하 이동.
	go(x + 1, y - 1, dep);
	// 하 이동.
	go(x + 1, y, dep);
	// 우하 이동.
	go(x + 1, y + 1, dep);
	 
	 return;
}

int main() {
	int start_x;
	int start_y;
	// 입력 받기. 
	cin >> N;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cin >> name[i][j];
			if (name[i][j] == 'K') K++;
			if (name[i][j] == 'P') {
				start_x = i;
				start_y = j;
				visit[i][j] = true;
			}
		}
	}
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cin >> alti[i][j];
		}
	}
	low = alti[start_x][start_y];
	high = alti[start_x][start_y];
	
	go(start_x, start_y, 1);
	
	
	
	
	return 0;
} 
