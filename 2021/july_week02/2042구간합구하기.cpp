// 2042 - ���� �� ���ϱ�.
// ���� ���� �������� ���׸�Ʈ Ʈ�� Ǯ�̶�� �Ѵ�. ���� ������ ����� ���� ���ϰ� �� ������ �׳� �貸�� Ǯ���µ�...
// ���� �ٷ� ��¡�ϵ��� ���׸�Ʈ Ʈ�� ������ ������. ��Ʃ�긦 ���� ��� ���� ���ظ� �ߴ�. 
// ���׸�Ʈ Ʈ���� �켱 buid�� �ϴ� ���� �ʿ��ϸ� ��ȸ(sum, max, min ������� ����), ������ �ϴ� �Լ����� �ʿ��ϴ�.
// ���� ���� �� �ð��ʰ��� �� �� �߻��ߴµ� update�� �Ϸ��� ���ڰ� long long�� �� �־ �ڷ��� ��ȯ�� �� �ߴ�. 
#include <iostream>
#include <vector>
using namespace std;

typedef long long ll;

int N, M, K;
ll num[1000001];
vector<ll> sgt;

// ���� ���� �ʿ��� ���׸�Ʈ Ʈ���� �����. 
ll build(int node, int left, int right) {
	// �� �̻� �ɰ� �� ���� ���´� �ش� node���� ��ȯ. 
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
	
	// ���׸�Ʈ Ʈ�� �ʱ�ȭ. 
	sgt.resize(N * 4);
	build(1, 0, N - 1);
	
	int a, b;
	ll c;
	for (int i = 0; i < M + K; i++) {
		cin >> a >> b >> c;
		// ���׸�Ʈ Ʈ�� update 
		if (a == 1) {
			update(b - 1, c, 1, 0, N - 1);
		} else { // ���׸�Ʈ Ʈ�� query 
			cout << query(b - 1, c - 1, 1, 0, N - 1) << "\n";
		}
	}
	
	
	
	return 0;
}
