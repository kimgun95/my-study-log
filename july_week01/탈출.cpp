#include <cstdio>
#include <queue>
#include <vector>
using namespace std;

typedef pair<int, int> pii;		// 좌표 담을 예정 
int r, c; // 행, 렬 
char forest[50][51]; // 지도 값 

pii ddg; // 두더지 좌표 
vector<pii> water; // 물 들의 좌표 
pii biber; // 굴 좌표 

queue<pii> water_q, ddg_q; // 물과 두더지 queue 생성 
int ans; // 정답 저장 변수 
// 방문 배열(0으로 초기화) 
int water_vt[50][50] = {0,}, ddg_vt[50][50] = {0,};
int dr[] = {-1, 1, 0,0}, dc[] = {0, 0, -1, 1}; // 상하좌우 계산 용도  

// 좌표가 지도에 유효한 좌표인지 확인하는 함수 
bool check_rc(int param_r, int param_c) {
	if (0 <= param_r && param_r < r && 0 <= param_c && param_c < c) return true;
	return false;
}

int main() {
	// 입력 처리 
	// 행,렬 
	scanf("%d %d", &r, &c);
	// 지도 
	for (int i = 0; i < r; i++)	{
		scanf("%s", forest[i]);
	}
	
	// 두더지의 시작점이 어디인지 확인
	for (int i = 0; i < r; i++) {
		for (int j = 0; j < c; j++) {
			if (forest[i][j] == 'S') {
				ddg = pii(i, j);
			}
		}
	}
	// 물 들은 어디에 있는지 확인
	for (int i = 0; i < r; i++) {
		for (int j = 0; j < c; j++) {
			if (forest[i][j] == '*') {
				water.push_back(pii(i,j));
			}
		}
	} 
	// 두더지의 굴
	for (int i = 0; i < r; i++) {
		for (int j = 0; j < c; j++) {
			if (forest[i][j] == '*') {
				biber = pii(i,j);
			}
		}
	}
	// 위 과정을 통해서 출력을 통해 제대로 입력이 되었는지 확인하면 됨. 
	//	printf("ddg: %d %d", ddg.first, ddg.second); 
	
	// 물 들과 두더지의 위치 들을 visited에 1로 저장 
	for (int i = 0; i< water.size(); i++) {
		pii cur_water = water[i];
		water_q.push(cur_water);
		water_vt[cur_water.first][cur_water.second] = 1;
	} 
	ddg_q.push(ddg);
	ddg_vt[ddg.first][ddg.second] = 1;
	
	// 물과 두더지를 탐색하면서 갈 수 있는지 없는지 판단
	// 두더지가 비버의 굴을 탐색하면 거리를 출력하고 끝
	// 두더지가 더 이상 탐색을 못하면 KAKTUS를 출력하고 끝
	while (!ddg_q.empty()) {
		// 물 이동
		// queue에서 하나를 꺼내고 상하좌우 로 이동
		// 비버의 목적지는 가지말고
		// 돌멩이도 가지 말고
		int water_qsz = water_q.size();
		for (int i = 0; i < water_qsz; i++) {
			pii cur_water = water_q.front();
			water_q.pop();
			for (int j = 0; j < 4; j++) {
				int new_r, new_c;
				new_r = cur_water.first + dr[j];
				new_c = cur_water.second + dc[j];
				// 유효한 좌표가 아닌 경우는 continue로 빠르게 다음 반복문을 실행해준다. 
				if (!check_rc(new_r, new_c)) continue;
				// 비버의 굴, 돌멩이, 물이 있는 곳은 이동 못하기에 유효하지 않아서 continue 
				if (forest[new_r][new_c] == 'D' || forest[new_r][new_c] == 'X' || water_vt[new_r][new_c] != 0) continue;
				// 유효한 위치로 물이 이동했다면 visited 변경 및 queue 에 추가를 한다. 
				water_vt[new_r][new_c] = water_vt[cur_water.first][cur_water.second] + 1;
				water_q.push(pii(new_r, new_c));
			}
		}
		// 두더지 이동
		// queue에서 하나를 꺼내고 상하좌우로 이동
		// 물은 가지 말고
		// 돌멩이도 가지말고
		// 목적지였으면? 찾은 것
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
                // 굴을 찾았을 때 
                if (forest[new_r][new_c] == 'D') {
                    // +1을 안하는 이유는 처음 시작이 1이었기 때문에 
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
	// 위 반복문에서 ans의 출력 없이 끝이 나면 KAKTUS 출력. 
	printf("KAKTUS");
	return 0; 
}
