// 9663 - Nqueen
// 진도상 따라 잡아야 하기에 코드를 보며 진행했음.
// 예전에 내가 푼 python코드를 보고 c++로 옮겨보려 했으나 도저히 코드가 이해가 안가 포기. 
// 강사님 코드랑 초반부 진행은 비슷했고 이후 진행은 강사님 코드가 이해하기 쉬워 그대로 사용.
// 완전탐색? 백트래킹? 을 사용한 것이고 탐색하던 곳을 재귀로 계속 파고 들다가 탐색이 끝나면
// visited를 다시 원래대로 재설정해야 하는 것은 항상 중요...! 
#include <iostream>
using namespace std;

int n, ans;
int chess[14][14];  // 초기화가 이미 0으로 되어있음  

// line : 0 ~ n - 1
void recur(int line) {
    // 종료조건. line 값이 n이 되는 것만 끝까지 queen을 채운 것이고 ans++ 및 return 
    if (line == n) {
        ans++;
        return;
    }
    // line어딘가에다가 queen을 놓아본다
    for (int i = 0 ; i < n ; i++) {
    	// 놓으려는 곳이 -1로 초기화 되어있지 않다면 놓지 못하기 때문에 continue 
        if (chess[line][i] != -1) continue;
        
        chess[line][i] = line;
        // line에 놓았으니까 상/하/좌/우/대각선에는 queen을 놓지 못하게 처리한다 
        // 좌/우 
        for (int x = 0 ; x < n ; x++) {
            if (chess[line][x] == -1) {
                chess[line][x] = line;
            }
        }
        // 하 (상이 제외인 이유는 이미 좌우 조건으로 윗줄에서 다른 숫자로 채워져있을 것이기 때문에) 
        for (int y = line ; y < n ; y++) {
            if (chess[y][i] == -1) {
                chess[y][i] = line;
            }
        }       
        // 대각선. 좌하로 가는 경로. 
        for (int y = line, x = i ; y < n && 0 <= x ; y++, x--) {
            if (chess[y][x] == -1) {
                chess[y][x] = line;
            }
        } // 대각선. 우하로 가는 경로. 
        for (int y = line, x = i ; y < n && x < n ; y++, x++) {
            if (chess[y][x] == -1) {
                chess[y][x] = line;
            }
        }

        // 다음 줄 queen을 놓아본다
        recur(line + 1);

		// 위에서 탐색을 모두 끝내고 오는 길이니 
        // queen이 처리한 흔적을 지운다. line 값을 다시 -1로. 
        for (int x = 0 ; x < n ; x++) {
            if (chess[line][x] == line) {
                chess[line][x] = -1;
            }
        }
        // 하
        for (int y = line ; y < n ; y++) {
            if (chess[y][i] == line) {
                chess[y][i] = -1;
            }
        }       
        // 대각선
        for (int y = line, x = i ; y < n && 0 <= x ; y++, x--) {
            if (chess[y][x] == line) {
                chess[y][x] = -1;
            }
        }
        for (int y = line, x = i ; y < n && x < n ; y++, x++) {
            if (chess[y][x] == line) {
                chess[y][x] = -1;
            }
        }
    }
}

int main() {
    // array fill
    for (int i = 0 ; i < 14 ; i++) {
        for (int j = 0 ; j < 14 ; j++) {
            chess[i][j] = -1;
        }
    }
    cin >> n;
    // todo
    recur(0);
    cout << ans;
}

