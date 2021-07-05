#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;

typedef pair<char, int> pci;

int N, K;
string word;
vector<string> words;
map<char, int> visited;
map<char, int> res;
int cases; 
int answer = 0;

int word_check(map<char, int> res) {
	int ans = 0;
	for (int i = 0; i < words.size(); i++) {
		int check = 0;
		for (int j = 0; j < words[i].size(); j++) {
			char c = words[i][j];
			if (!(c == 'a' || c == 'n' || c == 't' || c == 'i' || c == 'c')) {
				if (res[c] != 1) {
				check = 1;
				break;
				}
			}
			

		}
		if (check == 0) ans++;
	}
	return ans;
}
void Combination(vector<char> arr, vector<char> comb, int r, int index, int depth)
{
	
    if (r == 0)
    {
        for(int i = 0; i < comb.size(); i++) {
            res[comb[i]] = 1;
		}
            
        answer = max(answer, word_check(res));
        res.clear();
    }
    else if (depth == arr.size())  // depth == n // 계속 안뽑다가 r 개를 채우지 못한 경우는 이 곳에 걸려야 한다.
    {
        return;
    }
    else
    {
        // arr[depth] 를 뽑은 경우
        comb[index] = arr[depth];
        Combination(arr, comb, r - 1, index + 1, depth + 1);
        
        // arr[depth] 를 뽑지 않은 경우
        Combination(arr, comb, r, index, depth + 1);
    }
}

int main() {
	// N, K 입력. 
	cin >> N >> K;
	// N개 만큼 단어 입력. 
	for (int i = 0; i < N; i++) {
		cin >> word;
		word = word.substr(4, word.size());
		word = word.substr(0, word.size() - 4);
		words.push_back(word);
	}
	// 알파벳 visited 생성 
	for (int i = 97; i < 123; i++) {
		char c = i;
		if (c == 'a' || c == 'n' || c == 't' || c == 'i' || c == 'c') {
			visited.insert(pci(c, 1));
		} else {
			visited.insert(pci(c, 0));
		}
		res.insert(pci(c, 0));
	}
	
	 
//	cout << visited['a'] << endl;

	// 학습할 수 있는 새로운 문자의 개수 파악. 
	int count = 0;
	vector<char> arr;
	for (int i = 0; i < words.size(); i++) {
		for (int j = 0; j < words[i].size(); j++) {
			if (visited[words[i][j]] == 0) {
				visited[words[i][j]] = 1;
				arr.push_back(words[i][j]);
				count++;
			}
		}
	}
//	for (int i = 0; i < arr.size(); i++) {
//		cout << arr[i] << endl;
//	}

	int able = K - 5;
	if (able < 0) {
		cout << 0;
		return 0;
	}
    vector<char> comb(able);
	Combination(arr, comb, able, 0, 0);
	
	cout << answer << endl;
	

	
	
	
}
