#include <iostream>
using namespace std;

int N;
char name[50][50];
int alti[50][50];
int low = 1000000;
int high = 0;



int main() {
	
	// 입력 받기. 
	cin >> N;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cin >> name[i][j];
		}
	}
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cin >> alti[i][j];
		}
	}
	
	
	
	
	
	
	return 0;
} 
