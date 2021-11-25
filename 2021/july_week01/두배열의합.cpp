// 2143 - 두 배열의 합
// 풀다가 도저히 아이디어가 안나왔다. 
// vector의 upper_bound, lower_bound를 유용하게 이용하면 됐다.
// 모든 경우를 찾아서 vector에 때려 박은 후 함수를 활용하면 위치를 알아서 찾아내줘서 개꿀 기능이다...
// for 반복문에서 auto가 dev c++에서 실행이 안되는데  "-std=c++11" 를 컴파일러에 추가하여 해결했다. 
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int T;
int n, m;
int A[1000], B[1000];
vector<int> A_res, B_res;
long ans = 0;

// A와 B의 부배열의 합 모든 경우를 계산 하여 vector에 push_back 
void make_num() {
	for (int i = 0; i < n; i++) {
		int number = 0;
		for (int j = i; j < n; j++) {
			number += A[j];
			A_res.push_back(number);
		}
	}
	for (int i = 0; i < m; i++) {
		int number = 0;
		for (int j = i; j < m; j++) {
			number += B[j];
			B_res.push_back(number);
		}
	}
	return;
}

int main() {
	// 입력 받기. 
	cin >> T;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> A[i];
	}	
	cin >> m;
	for (int i = 0; i < m; i++) {
		cin >> B[i];
	}
	
	// 부배열의 합 모든 경우 계 산 
	make_num();
	// 뒤에서 경우의 수를 깔끔히 가져오기 위해 B_res를 sort 
	sort(B_res.begin(), B_res.end());
	
	// A_res에 있는 수 들 중에 중복도 있어서 처음에 아니지 않나? 했는데 숫자마다 만들어진 조합이 다르기 때문에 괜찮다. 
	for (auto num : A_res) {
		int diff = T - num;
		// upper_bound와 lower_bound 모두 iterator를 반환하며 둘 을 서로 빼서 차이 값을 받아낸다. 
		ans += upper_bound(B_res.begin(), B_res.end(), diff) - lower_bound(B_res.begin(), B_res.end(), diff);
	}
	cout << ans;
	
	
	return 0;
} 
