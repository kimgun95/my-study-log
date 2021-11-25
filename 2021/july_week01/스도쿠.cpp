// 2580 - 스도쿠
// 자료형 선언 부터 접근 까지 정말 근접했었다. 1퍼센트가 부족했음..!
// sudoku함수에서 이제 빈칸이 저장된 zero벡터에다가 1~9까지 숫자를 더해주면서 탐색을 하면 되었는데.
// 이때 받아온 depth로 zero에 접근할 수 있는 것을 생각 못해서 해매었다.
// 그렇게 접근을 한 뒤 1~9를 넣는 for 문을 만들면 되었던 것.
// check함수에서 구간 조건을 만들때 좌표에서 3으로 나눈 몫을 이용한 것이 좋은 아이디어..!
#include <iostream>
#include <vector>
using namespace std;

typedef pair<int, int> pii;
int arr[9][9];
int n = 0;
vector<pii> zero;

bool check(pii val) {
	int fir = val.first;
	int sec = val.second;
	int square_x = fir / 3;
	int square_y = sec / 3;
	
	// 수평 조건.
	for (int i = 0; i < 9; i++) {
		if (arr[fir][i] == arr[fir][sec] && i != sec) return false;
	}
	// 수직조건.
	for (int i = 0; i < 9; i++) {
		if (arr[i][sec] == arr[fir][sec] && i != fir) return false;
	}
	// 구역조건. 
	for (int i = square_x * 3; i < (square_x * 3) + 3; i++) {
		for (int j = square_y * 3; j < (square_y * 3) + 3; j++) {
			if (arr[i][j] == arr[fir][sec] && i != fir && j != sec) return false;
		}
	}
	return true;
}

void sudoku(int depth) {
	if (depth == n) {
		for (int i = 0; i < 9; i++) {
			for (int j = 0; j < 9; j++) {
				cout << arr[i][j] << " ";
			}
			cout << "\n";
		}
		exit(0);
	}
	int fir = zero[depth].first;
	int sec = zero[depth].second;
	for(int j = 1; j <= 9; j++) {
        arr[fir][sec] = j; // 1~9 까지의 숫자를 넣어봄
        if(check(zero[depth])) // 결과가 유효하면 다음 빈칸을 채우러 감
            sudoku(depth + 1);
    }
    arr[fir][sec] = 0;// 최적해를 못찾았을 경우 값 비워주기
    return;
}

int main() {
	// 스도쿠 입력 받기. 
	for (int i = 0; i < 9; i++) {
		for (int j = 0; j < 9; j++) {
			cin >> arr[i][j];
			if (arr[i][j] == 0) {
				n++;
				zero.push_back(pii(i, j));
			}
		}
	}
	sudoku(0);
} 
