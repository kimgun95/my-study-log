#include <cstdio>
#include <queue>
#include <vector>
using namespace std;

typedef pair<int, int> pii;		// ��ǥ ���� ���� 
int r, c; // ��, �� 
char forest[50][51]; // ���� �� 

pii ddg; // �δ��� ��ǥ 
vector<pii> water; // �� ���� ��ǥ 
pii biber; // �� ��ǥ 

queue<pii> water_q, ddg_q; // ���� �δ��� queue ���� 
int ans; // ���� ���� ���� 
// �湮 �迭(0���� �ʱ�ȭ) 
int water_vt[50][50] = {0,}, ddg_vt[50][50] = {0,};
int dr[] = {-1, 1, 0,0}, dc[] = {0, 0, -1, 1}; // �����¿� ��� �뵵  

// ��ǥ�� ������ ��ȿ�� ��ǥ���� Ȯ���ϴ� �Լ� 
bool check_rc(int param_r, int param_c) {
	if (0 <= param_r && param_r < r && 0 <= param_c && param_c < c) return true;
	return false;
}

int main() {
	// �Է� ó�� 
	// ��,�� 
	scanf("%d %d", &r, &c);
	// ���� 
	for (int i = 0; i < r; i++)	{
		scanf("%s", forest[i]);
	}
	
	// �δ����� �������� ������� Ȯ��
	for (int i = 0; i < r; i++) {
		for (int j = 0; j < c; j++) {
			if (forest[i][j] == 'S') {
				ddg = pii(i, j);
			}
		}
	}
	// �� ���� ��� �ִ��� Ȯ��
	for (int i = 0; i < r; i++) {
		for (int j = 0; j < c; j++) {
			if (forest[i][j] == '*') {
				water.push_back(pii(i,j));
			}
		}
	} 
	// �δ����� ��
	for (int i = 0; i < r; i++) {
		for (int j = 0; j < c; j++) {
			if (forest[i][j] == '*') {
				biber = pii(i,j);
			}
		}
	}
	// �� ������ ���ؼ� ����� ���� ����� �Է��� �Ǿ����� Ȯ���ϸ� ��. 
	//	printf("ddg: %d %d", ddg.first, ddg.second); 
	
	// �� ��� �δ����� ��ġ ���� visited�� 1�� ���� 
	for (int i = 0; i< water.size(); i++) {
		pii cur_water = water[i];
		water_q.push(cur_water);
		water_vt[cur_water.first][cur_water.second] = 1;
	} 
	ddg_q.push(ddg);
	ddg_vt[ddg.first][ddg.second] = 1;
	
	// ���� �δ����� Ž���ϸ鼭 �� �� �ִ��� ������ �Ǵ�
	// �δ����� ����� ���� Ž���ϸ� �Ÿ��� ����ϰ� ��
	// �δ����� �� �̻� Ž���� ���ϸ� KAKTUS�� ����ϰ� ��
	while (!ddg_q.empty()) {
		// �� �̵�
		// queue���� �ϳ��� ������ �����¿� �� �̵�
		// ����� �������� ��������
		// �����̵� ���� ����
		int water_qsz = water_q.size();
		for (int i = 0; i < water_qsz; i++) {
			pii cur_water = water_q.front();
			water_q.pop();
			for (int j = 0; j < 4; j++) {
				int new_r, new_c;
				new_r = cur_water.first + dr[j];
				new_c = cur_water.second + dc[j];
				// ��ȿ�� ��ǥ�� �ƴ� ���� continue�� ������ ���� �ݺ����� �������ش�. 
				if (!check_rc(new_r, new_c)) continue;
				// ����� ��, ������, ���� �ִ� ���� �̵� ���ϱ⿡ ��ȿ���� �ʾƼ� continue 
				if (forest[new_r][new_c] == 'D' || forest[new_r][new_c] == 'X' || water_vt[new_r][new_c] != 0) continue;
				// ��ȿ�� ��ġ�� ���� �̵��ߴٸ� visited ���� �� queue �� �߰��� �Ѵ�. 
				water_vt[new_r][new_c] = water_vt[cur_water.first][cur_water.second] + 1;
				water_q.push(pii(new_r, new_c));
			}
		}
		// �δ��� �̵�
		// queue���� �ϳ��� ������ �����¿�� �̵�
		// ���� ���� ����
		// �����̵� ��������
		// ������������? ã�� ��
		int ddg_qsz = ddg_q.size();
		for (int i = 0; i < ddg_qsz; i++) {
			pii cur_ddg = ddg_q.front();
			ddg_q.pop();
			for (int j = 0 ; j < 4 ; j++) {
                int new_r, new_c;
                new_r = cur_ddg.first + dr[j];
                new_c = cur_ddg.second + dc[j];
                if (!check_rc(new_r, new_c)) continue;
                if (forest[new_r][new_c] == 'X' || water_vt[new_r][new_c] != 0 || ddg_vt[new_r][new_c] != 0) continue;
                // ���� ã���� �� 
                if (forest[new_r][new_c] == 'D') {
                    // +1�� ���ϴ� ������ ó�� ������ 1�̾��� ������ 
                    ans = ddg_vt[cur_ddg.first][cur_ddg.second];
                    printf("%d", ans);
                    return 0;
                }
                else {
                    ddg_vt[new_r][new_c] = ddg_vt[cur_ddg.first][cur_ddg.second] + 1;
                    ddg_q.push(pii(new_r, new_c));
                }
            }
		} 
	}
	// �� �ݺ������� ans�� ��� ���� ���� ���� KAKTUS ���. 
	printf("KAKTUS");
	return 0; 
}
