// 1713 - 후보 추천하 기 
// 내가 해결하지 않았다. 진도를 맞추기 위해 잠깐 생각 후 선생님의 코드를 그냥 가져왔다.
// 내 첫 생각은 학생, 추천을 pair로 vector에다가 저장한 후 새로운 학생을 넣을 때 마다 이 vector를 search하면 어떨까 생각했다.
// 역시나 별로였던 생각... 하..;;
// 학생이 최대 100명이 있으니 학생들의 추천, 사진틀에 있을 위치, 등록된 시간 별로 따로 배열을 만들어 준 뒤
// 이를 비교하여 사진틀의 위치(position)를 가져오면 되었다. 
#include <iostream>
using namespace std;

int N;  // 사진틀의 갯수  
int pic_frame[20]; // 사진틀(자료구조) 0 ~ 19 index를 갖는다 
int num_cc; // 추천갯수  
int ord_cc[1000]; // 추천 순서

int cand_like[101]; //후보 추천 횟수
int cand_where[101]; // 후보가 어떤 사진틀에 걸려있는 지 
int cand_when[101]; // 후보가 사진틀에 언제 올라갔는지 

int get_pic_frame() {
    // 비어있는 틀이 있다면 return 
    for (int i = 0 ; i < N ; i++) {
        if (pic_frame[i] == 0) return i;
    }

    // 올라가있는 후보중에서 좋아요가 가장 작은후보
    // 같으면 오래전에 올라간후보
    int res = 0;    // 최종 반환할 사진틀의 위치  
    int min_like = 1000;    // 올라간 후보중에서 좋아요가 가장 작은 값을 얻기 위한 값  
    int old_when = 1000;    // 올라간 시간이 가장 오래된 값을 찾기 위한 값
    for (int i = 0; i < N; i++) {
        int cur = pic_frame[i];
        int tmp_like = cand_like[cur];
        int tmp_when = cand_when[cur];
        if (tmp_like < min_like) {
            min_like = tmp_like;
            old_when = tmp_when;
            res = i;
        }
        else if (tmp_like == min_like && tmp_when < old_when) {
            min_like = tmp_like;
            old_when = tmp_when;
            res = i;
        }
    }
    return res;
}

int main() {
	// 입력 받기. 
    cin >> N;
    cin >> num_cc;
    for (int i = 0 ; i < num_cc ; i++) {
        cin >> ord_cc[i];
    }

    // 초기화 
    for (int i = 1 ; i <= 100 ; i++) {
        cand_where[i] = -1;
        cand_when[i] = -1;
    }

    // 추천을 수행한다 .... num_cc만큼
    for (int i = 0 ; i < num_cc ; i++) {
        // ord_cc[i]
        int cur = ord_cc[i];
        // 후보가 사진틀에 올라가 있을까?
        if (cand_where[cur] != -1) {
            // 좋아요만 올려줌 
            cand_like[cur]++;
        }
        else {
            // 비어있는 또는 후보를 넣을 사진틀을 얻는다. 
            int pos = get_pic_frame();
            int delete_cand = pic_frame[pos];
            // delete_cand는 사진틀에서 내리면서, 좋아요도 초기화한다
            if (delete_cand != 0) {
                cand_where[delete_cand] = -1;
                cand_like[delete_cand] = 0;
            }
			// 새로운 후보를 사진틀에 추가        
            cand_where[cur] = pos;
            cand_like[cur] = 1;
            cand_when[cur] = i;
            pic_frame[pos] = cur;
        }       
    }

    // 정답을 출력한다
    // pic_frame을 조사해서, 누가 사진틀에 있는지확인하고,
    // 후보들을 모아서 번호가 증가하는 순서대로 출력한다..
    for (int i = 1 ; i <= 100 ; i++) {
        if (cand_where[i] != -1) {
            cout << i << " ";
        }
    }
}
