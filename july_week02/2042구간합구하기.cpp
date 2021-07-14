// 2042 - 구간 합 구하기.
// 구간 합은 전형적인 세그먼트 트리 풀이라고 한다. 어제 개념을 제대로 이해 안하고 한 문제를 그냥 배껴서 풀었는데...
// 오늘 바로 응징하듯이 세그먼트 트리 문제를 만났다. 유튜브를 보고 어느 정도 이해를 했다. 
// 세그먼트 트리를 우선 buid를 하는 것이 필요하며 조회(sum, max, min 등등으로 저장), 수정을 하는 함수들이 필요하다.
// 문제 제출 때 시간초과가 한 번 발생했는데 update를 하려는 숫자가 long long일 수 있어서 자료형 변환을 좀 했다. 
#include <iostream>
#include <vector>
using namespace std;

typedef long long ll;

int N, M, K;
ll num[1000001];
vector<ll> sgt;

// 구간 합이 필요한 세그먼트 트리를 만든다. 
ll build(int node, int left, int right) {
	// 더 이상 쪼갤 수 없는 상태는 해당 node값을 반환. 
	if (left == right) return sgt[node] = num[left];
	
	int mid = (left + right) / 2;
	sgt[node] = build(node * 2, left, mid) + build(node * 2 + 1, mid + 1, right);
	return sgt[node]; 
}

void update(int idx, ll newValue, int node, int left, int right) {
	if (left > idx || right < idx) return;
	if (left == right) {
		sgt[node] = newValue;
		return;
	}
	int mid = (left + right) / 2;
	update(idx, newValue, node * 2, left, mid);
	update(idx, newValue, node * 2 + 1, mid + 1, right);
	sgt[node] = sgt[node * 2] + sgt[node * 2 + 1];
}

ll query(int left, ll right, int node, int nodeLeft, int nodeRight) {
	if (nodeRight < left || nodeLeft > right) return 0;
	if (left <= nodeLeft && nodeRight <= right) return sgt[node];
	
	int mid = (nodeLeft + nodeRight) / 2;
	return query(left, right, node * 2, nodeLeft, mid) + query(left, right, node * 2 + 1, mid + 1, nodeRight);
}

int main() {
	cin >> N >> M >> K;
	for (int i = 0; i < N; i++) {
		cin >> num[i];
	}	
	
	// 세그먼트 트리 초기화. 
	sgt.resize(N * 4);
	build(1, 0, N - 1);
	
	int a, b;
	ll c;
	for (int i = 0; i < M + K; i++) {
		cin >> a >> b >> c;
		// 세그먼트 트리 update 
		if (a == 1) {
			update(b - 1, c, 1, 0, N - 1);
		} else { // 세그먼트 트리 query 
			cout << query(b - 1, c - 1, 1, 0, N - 1) << "\n";
		}
	}
	
	
	
	return 0;
}
