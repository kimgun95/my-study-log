// 1991 - 트리 순회
// 트리를 전위, 중위, 후위 순회의 경우로 나눠 출력하라고 해서... 아는 개념이긴 한데 오랜만에 직접 구현을 하라니까...
// 솔직히 어떻게 해야할지 몰랐다... 그런데 출력 위치를 바꿔주기만 하면 되는 거였다... 허허...
// 아 참 struct는 선언 후 사용시 배열처럼 index값이 들어가는 것이 아닌가??? 
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
