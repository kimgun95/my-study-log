// 2003 - 수들의 합2
// 내가 풀었다...! 단순히 for문 2개를 이용하여 해결한 문제라고 봐도 무방..! 
#include <iostream>
#include <vector>
using namespace std;

int N, M;
int num[30000]; // 숫자들을 입력 받음. 
vector<int> arr; // M보다 작은 숫자들의 idx를 저장. 
int ans = 0; // 출력할 결과 저장. 

// 합해서 M이 되는 경우의 수를 찾는다. 
void find() {
	// arr에 있는 숫자들로만 탐색을 진행. 
	for (int i = 0; i < arr.size(); i++) {
		int number = 0;
		// 다음 숫자들을 더하면서 M이 되는지 확인. 
		for (int j = arr[i]; j < N; j++) {
			number += num[j];
			if (number == M) {
				ans += 1;
				break;
			} else if (number > M) break;
		}
	}
	return;
}


int main() {
	// 입력 받기. 
	cin >> N >> M;
	for (int i = 0; i < N; i++) {
		cin >> num[i];
		// M보다 작은 숫자들의 idx를 미리 저장한다. (탐색 과정을 좀 더 단축시키기 위해) 
		if (num[i] <= M) {
			arr.push_back(i);
		} 
	}
	
	find();
	cout << ans;
	
	return 0;
} 
