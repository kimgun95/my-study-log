// 1072 - 게임
// 나는 시간초과, 틀렸습니다 가 나오길래 자료형 크기 때문인줄 알았다.
// 하지만 long long으로 자료형을 두면 초과할 일은 발생하지 않아서 괜찮았을거임.
// 우선 -1이 나올 수 있는 조건이 승률이 99일 때도 있다는 것이다.
// 승률은 99에서 절대 100으로 만들 수 없다. 처음 알았다...ㄹㅇ 빠가 다 된듯.
// 그리고 이분 탐색을 해야했다. 총 10억판을 더 한다고 생각하고 여기서 이분탐색을 통해 확률에 근사한 값을 찾으면 된다. 
#include <iostream>
using namespace std;

long long X, Y;
int start = 0;
int last = 1000000000;
int mid;
int ans = 0;

int main() {
	cin >> X >> Y;
	
	int res;
	res = (Y * 100) / X;
	
	if (X == Y || res >= 99) {
		cout << -1;
		return 0;
	}

	while (start <= last) {
		mid = (start + last) / 2;
		
		int win = ((Y + mid) * 100) / (X + mid);
		if (res >= win) {
			
			start = mid + 1;
		} else {
			ans = mid;
			last = mid - 1;
		}
	}
	cout << ans;
	return 0;
}
