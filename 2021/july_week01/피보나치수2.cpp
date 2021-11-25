// 2748 - 피보나치수2
// 재귀를 이용한 문제 풀이는 완벽했다. 다만 틀렸습니다 가 발생하여 자료형 때문이라는 것은 알았는데.
// 마지막에 fibo함수의 반환형을 long long으로 고치지 않은 것을 발견 못하였다 ㅠ.
// 아 처음에는 시간초과가 발생했는데 dp를 사용하지 않아서 였다. 한 번 계산한 fibo 값은 number배열에 저장하여 dp를 이용했다. 
#include <iostream>
using namespace std;

long long number[91];

long long fibo(int num) {
	if (num == 0 || num == 1) return num;
	if (number[num] != 0) return number[num];
	number[num] = fibo(num - 1) + fibo(num - 2);
	return number[num];
}

int main() {
	int n;
	cin >> n;
	
	long long ans;
	ans = fibo(n);
	cout << ans;
	
	return 0;
}
