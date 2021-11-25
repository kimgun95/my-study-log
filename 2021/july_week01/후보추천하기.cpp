// 1713 - �ĺ� ��õ�� �� 
// ���� �ذ����� �ʾҴ�. ������ ���߱� ���� ��� ���� �� �������� �ڵ带 �׳� �����Դ�.
// �� ù ������ �л�, ��õ�� pair�� vector���ٰ� ������ �� ���ο� �л��� ���� �� ���� �� vector�� search�ϸ� ��� �����ߴ�.
// ���ó� ���ο��� ����... ��..;;
// �л��� �ִ� 100���� ������ �л����� ��õ, ����Ʋ�� ���� ��ġ, ��ϵ� �ð� ���� ���� �迭�� ����� �� ��
// �̸� ���Ͽ� ����Ʋ�� ��ġ(position)�� �������� �Ǿ���. 
#include <iostream>
using namespace std;

int N;  // ����Ʋ�� ����  
int pic_frame[20]; // ����Ʋ(�ڷᱸ��) 0 ~ 19 index�� ���´� 
int num_cc; // ��õ����  
int ord_cc[1000]; // ��õ ����

int cand_like[101]; //�ĺ� ��õ Ƚ��
int cand_where[101]; // �ĺ��� � ����Ʋ�� �ɷ��ִ� �� 
int cand_when[101]; // �ĺ��� ����Ʋ�� ���� �ö󰬴��� 

int get_pic_frame() {
    // ����ִ� Ʋ�� �ִٸ� return 
    for (int i = 0 ; i < N ; i++) {
        if (pic_frame[i] == 0) return i;
    }

    // �ö��ִ� �ĺ��߿��� ���ƿ䰡 ���� �����ĺ�
    // ������ �������� �ö��ĺ�
    int res = 0;    // ���� ��ȯ�� ����Ʋ�� ��ġ  
    int min_like = 1000;    // �ö� �ĺ��߿��� ���ƿ䰡 ���� ���� ���� ��� ���� ��  
    int old_when = 1000;    // �ö� �ð��� ���� ������ ���� ã�� ���� ��
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
	// �Է� �ޱ�. 
    cin >> N;
    cin >> num_cc;
    for (int i = 0 ; i < num_cc ; i++) {
        cin >> ord_cc[i];
    }

    // �ʱ�ȭ 
    for (int i = 1 ; i <= 100 ; i++) {
        cand_where[i] = -1;
        cand_when[i] = -1;
    }

    // ��õ�� �����Ѵ� .... num_cc��ŭ
    for (int i = 0 ; i < num_cc ; i++) {
        // ord_cc[i]
        int cur = ord_cc[i];
        // �ĺ��� ����Ʋ�� �ö� ������?
        if (cand_where[cur] != -1) {
            // ���ƿ丸 �÷��� 
            cand_like[cur]++;
        }
        else {
            // ����ִ� �Ǵ� �ĺ��� ���� ����Ʋ�� ��´�. 
            int pos = get_pic_frame();
            int delete_cand = pic_frame[pos];
            // delete_cand�� ����Ʋ���� �����鼭, ���ƿ䵵 �ʱ�ȭ�Ѵ�
            if (delete_cand != 0) {
                cand_where[delete_cand] = -1;
                cand_like[delete_cand] = 0;
            }
			// ���ο� �ĺ��� ����Ʋ�� �߰�        
            cand_where[cur] = pos;
            cand_like[cur] = 1;
            cand_when[cur] = i;
            pic_frame[pos] = cur;
        }       
    }

    // ������ ����Ѵ�
    // pic_frame�� �����ؼ�, ���� ����Ʋ�� �ִ���Ȯ���ϰ�,
    // �ĺ����� ��Ƽ� ��ȣ�� �����ϴ� ������� ����Ѵ�..
    for (int i = 1 ; i <= 100 ; i++) {
        if (cand_where[i] != -1) {
            cout << i << " ";
        }
    }
}
