// 2748 - �Ǻ���ġ��2
// ��͸� �̿��� ���� Ǯ�̴� �Ϻ��ߴ�. �ٸ� Ʋ�Ƚ��ϴ� �� �߻��Ͽ� �ڷ��� �����̶�� ���� �˾Ҵµ�.
// �������� fibo�Լ��� ��ȯ���� long long���� ��ġ�� ���� ���� �߰� ���Ͽ��� ��.
// �� ó������ �ð��ʰ��� �߻��ߴµ� dp�� ������� �ʾƼ� ����. �� �� ����� fibo ���� number�迭�� �����Ͽ� dp�� �̿��ߴ�. 
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
