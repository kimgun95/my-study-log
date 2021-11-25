// 10845 - 큐
// 1년 전 풀이 그대로 제출. 시간 절약.
// 스택과 마찬가지로 이번엔 큐를 그대로 구현한 것. push, pop 등등... 
#include <iostream>
#include <stdio.h>
#include <queue>
#include <string>

using namespace std;

int main() {
	int test;
	queue<int> s;
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
				printf("%d\n", s.front());
				s.pop();
			}
		}
		else if (command == "front") {
			if (s.empty() == 1) {
				printf("-1\n");
			}
			else {
				printf("%d\n", s.front());
			}
		}
		else if (command == "back") {
			if (s.empty() == 1) {
				printf("-1\n");
			}
			else {
				printf("%d\n", s.back());
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
