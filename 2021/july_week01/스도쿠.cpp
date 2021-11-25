// 2580 - ������
// �ڷ��� ���� ���� ���� ���� ���� �����߾���. 1�ۼ�Ʈ�� ��������..!
// sudoku�Լ����� ���� ��ĭ�� ����� zero���Ϳ��ٰ� 1~9���� ���ڸ� �����ָ鼭 Ž���� �ϸ� �Ǿ��µ�.
// �̶� �޾ƿ� depth�� zero�� ������ �� �ִ� ���� ���� ���ؼ� �ظž���.
// �׷��� ������ �� �� 1~9�� �ִ� for ���� ����� �Ǿ��� ��.
// check�Լ����� ���� ������ ���鶧 ��ǥ���� 3���� ���� ���� �̿��� ���� ���� ���̵��..!
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
	
	// ���� ����.
	for (int i = 0; i < 9; i++) {
		if (arr[fir][i] == arr[fir][sec] && i != sec) return false;
	}
	// ��������.
	for (int i = 0; i < 9; i++) {
		if (arr[i][sec] == arr[fir][sec] && i != fir) return false;
	}
	// ��������. 
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
        arr[fir][sec] = j; // 1~9 ������ ���ڸ� �־
        if(check(zero[depth])) // ����� ��ȿ�ϸ� ���� ��ĭ�� ä�췯 ��
            sudoku(depth + 1);
    }
    arr[fir][sec] = 0;// �����ظ� ��ã���� ��� �� ����ֱ�
    return;
}

int main() {
	// ������ �Է� �ޱ�. 
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
