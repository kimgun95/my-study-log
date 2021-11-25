// 10828 - ����
// 1�� �� Ǯ�� �׳� �״�� �����մϴ�. �ð� ������ ����... 
// �⺻���� ������ �����ϴ� �����Դϴ�. ���� push, pop ���... 
#include <iostream>
#include <stdio.h>
#include <stack>
#include <string>

using namespace std;

int main() {
	int test;
	stack<int> s;
	string command;

	scanf("%d", &test);
	
	for (int i = 0; i < test; i++) {
	
		cin >> command;
		if (command == "push") {
			int num;
			scanf("%d", &num);
			s.push(num);
		}
		else if (command == "pop") {
			if (s.empty() == 1) {
				printf("-1\n");
			}
			else {
				printf("%d\n", s.top());
				s.pop();
			}
		}
		else if (command == "top") {
			if (s.empty() == 1) {
				printf("-1\n");
			}
			else {
				printf("%d\n", s.top());
			}
		}
		else if (command == "empty") {
			if (s.empty() == 1) {
				printf("1\n");
			}
			else {
				printf("0\n");
			}
		}
		else if (command == "size") {
			printf("%d\n", s.size());
		}
	}
	
	return 0;
}
