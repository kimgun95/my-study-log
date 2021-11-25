// 5693 - ���� �˻� Ʈ��
// ���� ���� Ǯ����...����;; �󸶸����� ����... ������ �Է� ���� ���� cin.eof()�� ���� �˻��ߴ�. 
#include <iostream>
#include <vector>
using namespace std;

vector<int> v;
int num;
int root;

typedef struct Node{
	int left = -1;
	int right = -1;
} node;

node n[1000000];

// ����� right�� �� �� �ִ� ��(node)�� ã�ƾ� ��. 
void find(int node, int val) {
	// ���� ���� node���� �۴ٸ� right�� �� �� ����. left�� ���� �ٽ� Ž��.
	// ũ�ٸ� right�� �̹� ��尡 ����ִ��� Ȯ��. ���ٸ� �־��ְ� �ִٸ� right�� ���� �ٽ� Ž��. 
	if (node > val) find(n[node].left, val);
	else {
		if (n[node].right != -1) find(n[node].right, val);
		else n[node].right = val;
	}
	return;
}

void build() {
	// ù ��° ���� root
	// ���� ��尡 ���� ��� ���� ������ ���� ����� left
	// ���� ��尡 ���� ��� ���� ũ�ٸ� root���� Ž���Ͽ� ��� node�� right���� ���� Ž��. 
	for (int i = 0; i < v.size(); i++) {
		if (i == 0) root = v[i];
		else if (v[i] < v[i - 1]) {
			n[v[i - 1]].left = v[i];
		} else {
			find(root, v[i]);
		}
	}
	return;
}

void postOrder(int node) {
	if (node == -1) return;
	postOrder(n[node].left);
	postOrder(n[node].right);
	cout << node << "\n";
	return;
}

int main() {
	
	// ������ �Է� ����. 
	while (true) {
		cin >> num;
		if (cin.eof()) {
			break;
		}
		v.push_back(num);
	}
	
	// ��带 ����ü�� �������ش�. (�׷��� �����) 
	build();
	// ���� ��ȸ ���. 
	postOrder(root);

	
	
	return 0;
} 
