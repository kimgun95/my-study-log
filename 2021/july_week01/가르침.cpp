// 1062 - ����ħ
// �ٺ� ���� ó���� �Է¹��� ���ڵ��� ���ĺ��� �����ؼ�... �̸� combination�Ͽ� ���� ����� ���� ���� ��...
// ���� ����� ������ �ܾ���� ���� �� �ִ� �ִ밪�� ������... �� ���� �ߴµ� �ٺ� ���� ���̾���.
// �ذ���� �����ߴ�. ��� ���ĺ��� ��츦 �������� �Ǿ��� ��.
// ������ ���� visited�� map���� ����鼭 �����Ÿ��� �ߴµ� �̰͵� �ƴϾ��� �׳� bool������ ����� �ϸ� �Ǿ���.
// ��͸� �̿��� DFS�� �ϸ� �Ǿ��� ���� ��Ͱ� �ͼ�ġ �ʴٺ��� ���̵�� ���� �������� �ʾҴ� ��... 
// ���ĺ��� ������ K - 5���� ä���� �� check�� ���� �ܾ ������ �ȴ�. 
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

typedef pair<char, int> pci;

int N, K;
string word;
vector<string> words;
bool visited[26];
int able;
int res = 0;

void word_check() {
	int ans = 0;
	// N���� �ܾ ���߰���. 
	for (int i = 0; i < N; i++) {
		bool check = false;
		// �ܾ��� ���ĺ� �ϳ��� �������߰���. visited�� �ִ���. 
		for (int j = 0; j < words[i].length(); j++) {
			// ���ٸ� ���� �� ������ �ٷ� break; 
			if (!visited[words[i][j] - 97]) {
				check = true;
				break;
			}
		}
		// �ܾ ���� �� �ִٸ� ans++ 
		if (!check) ans++;
	}
	res = max(res, ans);
	return;
}

void DFS(int idx, int size) {
	// size�� K�� �����ϸ� word_check�� ���� �� ���� �ܾ ���� �� �ִ��� Ȯ��. 
	if (able == size) {
		word_check();
		return;
	}
	// ���ĺ� �ϳ��� true�� ����� ����� �� ����. 
	for (int i = idx; i < 26; i++) {
		if (visited[i] == false) {
			visited[i] = true;
			DFS(i, size + 1);
			visited[i] = false;
		}
	}
}

int main() {
	// N, K �Է�. 
	cin >> N >> K;
	// N�� ��ŭ �ܾ� �Է�. 
	for (int i = 0; i < N; i++) {
		cin >> word;
		// �ܾ���� �� �ڸ� �߶� vector�� �־���. 
		word = word.substr(4, word.size());
		word = word.substr(0, word.size() - 4);
		words.push_back(word);
	}
	// ���ĺ� visited ���� 
	visited['a' - 97] = true;
	visited['c' - 97] = true;
	visited['i' - 97] = true;
	visited['n' - 97] = true;
	visited['t' - 97] = true;
	
	// �Ұ����� ���, ��� �Ǵ� ���� ������ ����ع�����. 
	able = K - 5;
	if (able < 0) {
		cout << 0;
		return 0;
	}
	if (K == 26) {
		cout << N;
		return 0;
	}
	
	// ��͸� �̿��� DFS. ��� ���ĺ��� ��츦 ��������. 
    DFS(0, 0); 
	
	cout << res << endl;
}
