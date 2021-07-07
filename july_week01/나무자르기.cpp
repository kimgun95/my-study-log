#include <iostream>
using namespace std;

int N, M;
int tree[1000000];
int high = 0;
int ans;

int cut() {
	for (int i = high - 1; i >= 0; i--) {
		int len = 0;
		for (int j = 0; j < N; j++) {
			if (tree[j] > i) len += tree[j] - i;
		}
		if (len >= M) return i;
	}
}


int main() {
	// 입력 받기. 
	cin >> N >> M;
	for (int i = 0; i < N; i++) {
		cin >> tree[i];
		if (tree[i] > high) high = tree[i];
	}
	ans = cut();
	cout << ans;
	return 0;
} 
