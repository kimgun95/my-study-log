// 1062 - 가르침
// 바보 같이 처음에 입력받은 문자들의 알파벳을 추출해서... 이를 combination하여 나온 경우의 수를 돌린 후...
// 나온 경우의 수에서 단어들을 읽을 수 있는 최대값을 구하자... 로 접근 했는데 바보 같은 짓이었다.
// 해결법은 간단했다. 모든 알파벳의 경우를 돌려보면 되었던 것.
// 심지어 나는 visited를 map으로 만들면서 개짓거리를 했는데 이것도 아니었고 그냥 bool형으로 만들어 하면 되었음.
// 재귀를 이용한 DFS를 하면 되었고 역시 재귀가 익숙치 않다보니 아이디어 조차 떠오르지 않았던 것... 
// 알파벳의 개수는 K - 5개가 채워질 때 check를 통해 단어를 읽으면 된다. 
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
	// N개의 단어를 봐야겠죠. 
	for (int i = 0; i < N; i++) {
		bool check = false;
		// 단어의 알파벳 하나씩 따져봐야겠죠. visited에 있는지. 
		for (int j = 0; j < words[i].length(); j++) {
			// 없다면 읽을 수 없으니 바로 break; 
			if (!visited[words[i][j] - 97]) {
				check = true;
				break;
			}
		}
		// 단어를 읽을 수 있다면 ans++ 
		if (!check) ans++;
	}
	res = max(res, ans);
	return;
}

void DFS(int idx, int size) {
	// size가 K를 만족하면 word_check를 통해 몇 개의 단어를 읽을 수 있는지 확인. 
	if (able == size) {
		word_check();
		return;
	}
	// 알파벳 하나씩 true로 만들며 경우의 수 생성. 
	for (int i = idx; i < 26; i++) {
		if (visited[i] == false) {
			visited[i] = true;
			DFS(i, size + 1);
			visited[i] = false;
		}
	}
}

int main() {
	// N, K 입력. 
	cin >> N >> K;
	// N개 만큼 단어 입력. 
	for (int i = 0; i < N; i++) {
		cin >> word;
		// 단어들의 앞 뒤를 잘라서 vector에 넣어줌. 
		word = word.substr(4, word.size());
		word = word.substr(0, word.size() - 4);
		words.push_back(word);
	}
	// 알파벳 visited 생성 
	visited['a' - 97] = true;
	visited['c' - 97] = true;
	visited['i' - 97] = true;
	visited['n' - 97] = true;
	visited['t' - 97] = true;
	
	// 불가능한 경우, 모두 되는 경우는 빠르게 출력해버리기. 
	able = K - 5;
	if (able < 0) {
		cout << 0;
		return 0;
	}
	if (K == 26) {
		cout << N;
		return 0;
	}
	
	// 재귀를 이용한 DFS. 모든 알파벳의 경우를 돌려본다. 
    DFS(0, 0); 
	
	cout << res << endl;
}
