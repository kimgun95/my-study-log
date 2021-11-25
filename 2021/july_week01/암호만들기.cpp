//���� 1759�� - ��ȣ �����
//���� ���� ������ �ڵ带 �״�� �����Դµ� ���� ������ Ǭ �ڵ带 �״�� ������.
// DFS ��͸� �̿��Ͽ� Ǯ �� ���ٰ� �����ߴ� �� �¾���.
// �̶� ���� �ٸ� ���� �ڵ带 �״�� ��� �� �� ����. ���� ���� ���� ����� �� ���� ������ ���̵�� ����. 
// vector�� ���� Ž���� ���ĺ��� �־�δ� �뵵�� ���� ���� ����. 
#include <iostream>
#include <algorithm> //sort ���. 
#include <vector>
#include <set>
using namespace std;

#define MAX 15

char arr[MAX]; //��ȣ�� �� ���ĺ� �Է�
set<char> moeum_set; //���� ���� set�Լ��� ����
vector<char> dfs_vec; //dfs�� Ž���� ���ĺ��� �־���
int L, C; //��ȣ ����, ���ĺ� �� ����

// ��ȣ�� ����� ���� dfs
void dfs(int depth, int moeum, int jaeum, int idx) {
	// depth��  L - 1 �̸� ��� �� return 
	if (depth == L - 1) {
		// ������ 1�� �̻� , ������ 2���̻� Ȯ�� 
		if (moeum < 1 || jaeum < 2) return;
		// ��� 
		for (int i = 0; i < L; i++)
			cout << dfs_vec[i];
		cout << "\n";
		return;
	}
	
	// �ݷ� üũ 
	// 1. idx �� ���� �ʰ��� ����(���� depth�� ���� ���ϰ� idx �迭 ���������� ���� ��ȣ�� ���� �� ����)
	// 2. �ʿ��� ������ ������ ���� ������ �������� ũ�� ������
	if (idx >= C) return;
	if (L - (moeum + jaeum) > C - idx) return;


	// ���� �ܾ� �߰�. 
	for (int i = idx; i < C; i++) {
		dfs_vec.push_back(arr[i]);
		//dfs�� ���ȣ�� �Ҷ� depth�� �÷���
		// �����̸�.  
		if (moeum_set.find(arr[i]) == moeum_set.end())
			dfs(depth + 1, moeum, jaeum + 1, i + 1);
		// �����̸� 
		else
			dfs(depth + 1, moeum + 1, jaeum, i + 1);
		dfs_vec.pop_back();
	}
}

int main() {
	ios::sync_with_stdio(false);
	// ���� �� �ʱ�ȭ. 
	moeum_set.insert('a'); 
	moeum_set.insert('e'); 
	moeum_set.insert('i'); 
	moeum_set.insert('o'); 
	moeum_set.insert('u'); 
	
	// �Է� �ޱ�. 
	cin >> L >> C;
	for (int i = 0; i < C; i++) cin >> arr[i];
	// ���ϰ� ���ĺ� ó���� ����. 
	sort(arr, arr + C);

	for (int i = 0; i < C; i++) {
		dfs_vec.push_back(arr[i]);
		//dfs�� �����̴ϱ� ù ��° index�� depth�� 0�� ����.
		// �����̸�. set�ڷ����� find �Լ��� ��Ҹ� ã�� ���ϸ� end �Լ��� ���� ���� ��ȯ�Ѵ�.
		if (moeum_set.find(arr[i]) == moeum_set.end())
			dfs(0, 0, 1, i + 1);
		// �����̸� 
		else
			dfs(0, 1, 0, i + 1);
		// �׻� Ž���� ������ pop 
		dfs_vec.pop_back();
	}

	return 0;
}
