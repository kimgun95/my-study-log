// 1991 - Ʈ�� ��ȸ
// Ʈ���� ����, ����, ���� ��ȸ�� ���� ���� ����϶�� �ؼ�... �ƴ� �����̱� �ѵ� �������� ���� ������ �϶�ϱ�...
// ������ ��� �ؾ����� ������... �׷��� ��� ��ġ�� �ٲ��ֱ⸸ �ϸ� �Ǵ� �ſ���... ����...
// �� �� struct�� ���� �� ���� �迭ó�� index���� ���� ���� �ƴѰ�??? 
#include <iostream>
using namespace std;

struct node {
	char left;
	char right;
};


int n;
struct node arr[27];

void preOrder(char root) {
	if (root == '.') return;
	cout << root;
	preOrder(arr[root].left);
	preOrder(arr[root].right);
}

void inOrder(char root) {
	if (root == '.') return;
	inOrder(arr[root].left);
	cout << root;
	inOrder(arr[root].right);
}

void postOrder(char root) {
	if (root == '.') return;
	postOrder(arr[root].left);
	postOrder(arr[root].right);
	cout << root;
}

int main() {
	cin >> n;
	char ch, l, r;
	
	for (int i = 0; i < n; i++) {
		cin >> ch >> l >> r;
		arr[ch].left = l;
		arr[ch].right = r;
	}
	

	preOrder('A');
	cout << "\n";
	inOrder('A');
	cout << "\n";
	postOrder('A');
	
	
	return 0;
}
