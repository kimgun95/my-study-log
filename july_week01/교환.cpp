// 1039 - 교환 
// 진도 때문에 강사님의 코드로 진행을 했다. 중복 경우가 next_q에 추가되지 않는 상황만을 해결하였다.
// visit을 만들어 해당 숫자를 방문함을 알면 추가하지 않으면 되었다. 이때 k번 째에 동일 숫자가 나오냐를 판단해야 하기 때문에
// 2중 배열로 선언하여 해결.
// 알파벳을 일일이 모두 바꿔보는 완전 탐색이었고 conv 함수에서 사용한 sprintf가 이해하기 좀 어려웠다. 
#include <iostream>
#include <vector>
#include <queue> 
using namespace std;

int visit[1000000][11] = {0,};

// 문자열 형식으로 된 숫자를 숫자로 변환하기. 
int tonum(char arr[]) {
    int res = 0;
    for (int i = 0 ; arr[i] ; i++) {
        res *= 10;
        res += arr[i] - '0';
    }
    return res;
}

// num 숫자에서 l, r 위치 숫자를 서로 swap (convert) 
int conv(int num, int l, int r) {
    // l과 r의 체크가 안되어있음 
    // 처음에 num의 자리수는 정해져있기때문에 그걸 이용하면  됨 
    // arr
    char buf[16];
    sprintf(buf, "%d", num);
    char tmp;
    // swap
    tmp = buf[l];
    buf[l] = buf[r];
    buf[r] = tmp;
    // 앞자리가 0이 아닌지 체크도.. 
    if (buf[0] == '0') return 0;
    return tonum(buf);
}

int n, k;

bool isok(int num) {
    // 예외가 되는 것들은 바로처리  
    // 1 ~ 9 ==> 교환이 안됨 ==> -1
    if (num < 10) return false;
    // 10, 20, .. .90 ==> 교환이 안됨 ==> -1
    if (num < 100 && num % 10 == 0) return false;
    return true;
}

// 숫자의 길이 계산. 
int get_num_len(int num) {
    int len = 0;
    while (num > 0) {
        len++;
        num /= 10;
    }
    return len;
}

int main() {    
    // todo - 완전탐색 
    // 숫자를 직접 교환하는 로직
    // 교환해서 단계별로 탐색해가는 로직 
    cin >> n >> k; 
    if (n == 1000000) {
        cout << n;
        return 0;
    }
    if (!isok(n)) {
        cout << -1;
        return 0;
    }

    queue<int> q;
    q.push(n);
    for (int i = 0 ; i < k ; i++) {
        // q --> next_q --> q
        // 단계별로 처리하기 위해서 
        // 다음번 작업을 하기전에 임시로 저장하는 곳
        vector<int> next_q;

        while (!q.empty()) {
            int cur = q.front();
            q.pop();
            int len = get_num_len(cur);
			// cur 숫자에서 한 번 교환할 수 있는 경우를 모두 체크. 
            for (int s = 0 ; s < len ; s++) {
                for (int e = s + 1 ; e < len ; e++) {
                	// conv함수를 통해 숫자 swap 
                    int next_num = conv(cur, s, e);
                    // 맨 앞이 0이 온 경우 continue 
                    if (next_num == 0) continue;
                    // 같은 k번 째 상황에 같은 next_num이 나오게 되면 중복이므로 continue 
                    if (visit[next_num][i + 1] == 1) continue;
                    // k번 째 상황에 나온 next_num의 visit 설정. 
                	visit[next_num][i + 1] = 1;
                	next_q.push_back(next_num);
                }
            }
        }
        for (int i = 0 ; i < next_q.size() ; i++) {
            q.push(next_q[i]);
        }
    }
    // k번을 돌렸기 때문에 q에남아 있는 것들은 k번을 수행하고 남은 숫자들이고
    // q에 남은것 중에 가장 큰것을 출력하면 됨
    int ans = 0;
    while (!q.empty()) {
        int cur = q.front();
        q.pop();
        if (ans < cur) ans = cur;
    }
    cout << ans;
}
