// 1039 - ��ȯ 
// ���� ������ ������� �ڵ�� ������ �ߴ�. �ߺ� ��찡 next_q�� �߰����� �ʴ� ��Ȳ���� �ذ��Ͽ���.
// visit�� ����� �ش� ���ڸ� �湮���� �˸� �߰����� ������ �Ǿ���. �̶� k�� °�� ���� ���ڰ� �����ĸ� �Ǵ��ؾ� �ϱ� ������
// 2�� �迭�� �����Ͽ� �ذ�.
// ���ĺ��� ������ ��� �ٲ㺸�� ���� Ž���̾��� conv �Լ����� ����� sprintf�� �����ϱ� �� �������. 
#include <iostream>
#include <vector>
#include <queue> 
using namespace std;

int visit[1000000][11] = {0,};

// ���ڿ� �������� �� ���ڸ� ���ڷ� ��ȯ�ϱ�. 
int tonum(char arr[]) {
    int res = 0;
    for (int i = 0 ; arr[i] ; i++) {
        res *= 10;
        res += arr[i] - '0';
    }
    return res;
}

// num ���ڿ��� l, r ��ġ ���ڸ� ���� swap (convert) 
int conv(int num, int l, int r) {
    // l�� r�� üũ�� �ȵǾ����� 
    // ó���� num�� �ڸ����� �������ֱ⶧���� �װ� �̿��ϸ�  �� 
    // arr
    char buf[16];
    sprintf(buf, "%d", num);
    char tmp;
    // swap
    tmp = buf[l];
    buf[l] = buf[r];
    buf[r] = tmp;
    // ���ڸ��� 0�� �ƴ��� üũ��.. 
    if (buf[0] == '0') return 0;
    return tonum(buf);
}

int n, k;

bool isok(int num) {
    // ���ܰ� �Ǵ� �͵��� �ٷ�ó��  
    // 1 ~ 9 ==> ��ȯ�� �ȵ� ==> -1
    if (num < 10) return false;
    // 10, 20, .. .90 ==> ��ȯ�� �ȵ� ==> -1
    if (num < 100 && num % 10 == 0) return false;
    return true;
}

// ������ ���� ���. 
int get_num_len(int num) {
    int len = 0;
    while (num > 0) {
        len++;
        num /= 10;
    }
    return len;
}

int main() {    
    // todo - ����Ž�� 
    // ���ڸ� ���� ��ȯ�ϴ� ����
    // ��ȯ�ؼ� �ܰ躰�� Ž���ذ��� ���� 
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
        // �ܰ躰�� ó���ϱ� ���ؼ� 
        // ������ �۾��� �ϱ����� �ӽ÷� �����ϴ� ��
        vector<int> next_q;

        while (!q.empty()) {
            int cur = q.front();
            q.pop();
            int len = get_num_len(cur);
			// cur ���ڿ��� �� �� ��ȯ�� �� �ִ� ��츦 ��� üũ. 
            for (int s = 0 ; s < len ; s++) {
                for (int e = s + 1 ; e < len ; e++) {
                	// conv�Լ��� ���� ���� swap 
                    int next_num = conv(cur, s, e);
                    // �� ���� 0�� �� ��� continue 
                    if (next_num == 0) continue;
                    // ���� k�� ° ��Ȳ�� ���� next_num�� ������ �Ǹ� �ߺ��̹Ƿ� continue 
                    if (visit[next_num][i + 1] == 1) continue;
                    // k�� ° ��Ȳ�� ���� next_num�� visit ����. 
                	visit[next_num][i + 1] = 1;
                	next_q.push_back(next_num);
                }
            }
        }
        for (int i = 0 ; i < next_q.size() ; i++) {
            q.push(next_q[i]);
        }
    }
    // k���� ���ȱ� ������ q������ �ִ� �͵��� k���� �����ϰ� ���� ���ڵ��̰�
    // q�� ������ �߿� ���� ū���� ����ϸ� ��
    int ans = 0;
    while (!q.empty()) {
        int cur = q.front();
        q.pop();
        if (ans < cur) ans = cur;
    }
    cout << ans;
}
