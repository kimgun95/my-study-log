//백준 1759번 - 암호 만들기
//역시 진도 때문에 코드를 그대로 가져왔는데 내가 예전에 푼 코드를 그대로 가져옴.
// DFS 재귀를 이용하여 풀 것 같다고 생각했는 데 맞았음.
// 이때 내가 다른 분의 코드를 그대로 들고 온 것 같음. 모음 셋을 따로 만들어 둔 것이 괜찮은 아이디어 같음. 
// vector를 만들어서 탐색한 알파벳을 넣어두는 용도도 좋은 생각 같음. 
#include <iostream>
#include <algorithm> //sort 사용. 
#include <vector>
#include <set>
using namespace std;

#define MAX 15

char arr[MAX]; //암호가 될 알파벳 입력
set<char> moeum_set; //모음 셋을 set함수로 설정
vector<char> dfs_vec; //dfs로 탐색한 알파벳을 넣어줌
int L, C; //암호 갯수, 알파벳 총 갯수

// 암호를 만들기 위한 dfs
void dfs(int depth, int moeum, int jaeum, int idx) {
	// depth가  L - 1 이면 출력 및 return 
	if (depth == L - 1) {
		// 모음은 1개 이상 , 자음은 2개이상 확인 
		if (moeum < 1 || jaeum < 2) return;
		// 출력 
		for (int i = 0; i < L; i++)
			cout << dfs_vec[i];
		cout << "\n";
		return;
	}
	
	// 반례 체크 
	// 1. idx 의 범위 초과시 종료(위의 depth를 만족 못하고 idx 배열 마지막까지 오면 암호를 만들 수 없음)
	// 2. 필요한 숫자의 개수가 남은 숫자의 개수보다 크면 끝내기
	if (idx >= C) return;
	if (L - (moeum + jaeum) > C - idx) return;


	// 다음 단어 추가. 
	for (int i = idx; i < C; i++) {
		dfs_vec.push_back(arr[i]);
		//dfs를 재귀호출 할때 depth를 늘려줌
		// 자음이면.  
		if (moeum_set.find(arr[i]) == moeum_set.end())
			dfs(depth + 1, moeum, jaeum + 1, i + 1);
		// 모음이면 
		else
			dfs(depth + 1, moeum + 1, jaeum, i + 1);
		dfs_vec.pop_back();
	}
}

int main() {
	ios::sync_with_stdio(false);
	// 모음 셋 초기화. 
	moeum_set.insert('a'); 
	moeum_set.insert('e'); 
	moeum_set.insert('i'); 
	moeum_set.insert('o'); 
	moeum_set.insert('u'); 
	
	// 입력 받기. 
	cin >> L >> C;
	for (int i = 0; i < C; i++) cin >> arr[i];
	// 편하게 알파벳 처음에 정렬. 
	sort(arr, arr + C);

	for (int i = 0; i < C; i++) {
		dfs_vec.push_back(arr[i]);
		//dfs의 시작이니까 첫 번째 index인 depth는 0인 것임.
		// 자음이면. set자료형은 find 함수로 요소를 찾지 못하면 end 함수와 같은 값을 반환한다.
		if (moeum_set.find(arr[i]) == moeum_set.end())
			dfs(0, 0, 1, i + 1);
		// 모음이면 
		else
			dfs(0, 1, 0, i + 1);
		// 항상 탐색이 끝나면 pop 
		dfs_vec.pop_back();
	}

	return 0;
}
