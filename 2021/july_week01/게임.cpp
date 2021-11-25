// 1103 - ����
// DFS�� ������ �ߴ�. �õ��� �������� ���� �ݺ��� �� �� �ִ� ��츦 �������ߴ�. �� visited�� �����ߴ�.
// visited�� Ȱ���Ͽ� �Ѵ��ص� DFS�δ� Ǯ���� �ʴ� �����̴�. �Ƹ� �ص� ������.
// ���� DP�� �Բ� ������Ѿ� �ϴ� ����. �ش� ��ǥ���� �ִ�� ������ �� �ִ� Ƚ���� �����ϸ� �ȴ�. 
#include <iostream>
using namespace std;

int N, M;
int arr[50][50]; // ���� 
bool visit[50][50]; // �湮 ���� 
int DP[50][50]; // �ִ� ������ �� �ִ� Ƚ�� ����. 
int dr[] = {-1, 1, 0, 0}, dc[] = {0, 0, -1, 1}; // �����¿� ��� �뵵. 

int ans = 0;


int DFS(int row, int col) {
	if (row < 0 || row >= N || col < 0 || col >= M || arr[row][col] == 0) return 0;
	// �̹� �湮�� ���� ���� ��ȯ�� �����ϱ� ������ -1 ��� �� ���α׷� ����. 
	if (visit[row][col] == true) {
		cout << -1 << endl;
		exit(0);
	}
	// DP�� -1�� �ƴ϶�� ������ �̹� �� �� �ִ� �ִ��θ� ����� �����̱� ������ �ٷ� ��ȯ. 
	if (DP[row][col] != -1) return DP[row][col];
	// DP�� 0���� ����, �湮 üũ�� �� �� DP�� ����. 
	visit[row][col] = true;
	DP[row][col] = 0;
	// �����¿� �̵��� ���� DP�� ���. 
	for (int i = 0; i < 4; i++) {
		int row_num = row + (dr[i] * arr[row][col]);
		int col_num = col + (dc[i] * arr[row][col]);
		// �̵��� �ϴ� ���̴� +1 Ƚ�� ����. 
		DP[row][col] = max(DP[row][col], DFS(row_num, col_num) + 1);
	}
	// ��� �������� �湮 üũ �ʱ�ȭ 
	visit[row][col] = false;
	return DP[row][col];
}

int main() {
	// �Է� �ޱ�. 
	cin >> N >> M;
    for (int i = 0; i < N; i++)
    {
        string s;
		cin >> s;
		// �Է� ���� string�� arr�� ������������ ����. 
        for (int j = 0; j < s.length(); j++)
        {
            if (s[j] == 'H') arr[i][j] = 0;
            else arr[i][j] = s[j] - '0';
        }
    }
    // DP�� -1�� ��� �ʱ�ȭ. 
    for (int i = 0; i < N; i++) {
    	for (int j = 0; j < M; j++) {
    		DP[i][j] = -1;
		}
	}
    
    // DFS ����. 
    ans = DFS(0,0); 
    
    cout << ans;

} 
