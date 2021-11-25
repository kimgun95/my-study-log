// 5693 - 이진 검색 트리
// 내가 직접 풀었다...ㅎㅎ;; 얼마만인지 허허... 하지만 입력 종료 조건 cin.eof()는 몰라서 검색했다. 
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

// 노드의 right로 갈 수 있는 곳(node)을 찾아야 함. 
void find(int node, int val) {
	// 따라서 현재 node보다 작다면 right로 갈 수 없음. left로 가서 다시 탐색.
	// 크다면 right에 이미 노드가 들어있는지 확인. 없다면 넣어주고 있다면 right로 가서 다시 탐색. 
	if (node > val) find(n[node].left, val);
	else {
		if (n[node].right != -1) find(n[node].right, val);
		else n[node].right = val;
	}
	return;
}

void build() {
	// 첫 번째 노드는 root
	// 현재 노드가 이전 노드 보다 작으면 이전 노드의 left
	// 현재 노드가 이전 노드 보다 크다면 root부터 탐색하여 어느 node의 right으로 둘지 탐색. 
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
	
	// 노드들을 입력 받음. 
	while (true) {
		cin >> num;
		if (cin.eof()) {
			break;
		}
		v.push_back(num);
	}
	
	// 노드를 구조체로 연결해준다. (그래프 만들기) 
	build();
	// 후위 순회 출력. 
	postOrder(root);

	
	
	return 0;
} 
