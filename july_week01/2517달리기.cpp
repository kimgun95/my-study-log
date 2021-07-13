// 2517 - 달리기
// 세그먼트 트리 이해해야함. 지금 이해 못함.... 
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

typedef pair<int, int> pii;
 
int N;
vector<pii> v;

bool comp_ability(pair<int, int> a, pair<int, int> b) {
	return a.second > b.second;
}

bool comp_index(pair<int, int> a, pair<int, int> b) {
	return a.first < b.first;
}

class Segment_tree
{
	public:
		Segment_tree() {}
		Segment_tree(int tree_size) {
			tree.resize(tree_size);
		}
		
		int query(int cur, int start, int end, int left, int right) {
			if (end < left || right < start) return 0;
			
			if (left <= start && end <= right) return tree[cur];
			
			int mid = (start + end) / 2;
			return query(cur * 2, start, mid, left, right) + query(cur * 2 + 1, mid + 1, end, left, right);

		}
		int update(int cur, int start, int end, int target, int val) {
			if (target < start || end < target) return tree[cur];
			
			if (start == end) {
				tree[cur] += val;
				return tree[cur];
			}
			int mid = (start + end) / 2;
			return tree[cur] = update(cur * 2, start, mid, target, val) + update(cur * 2 + 1, mid + 1, end, target, val);
		
		}
		vector<int> tree;
};

int main() {
	cin >> N;
	int num;
	for (int i = 0; i < N; i++) {
		
		cin >> num;
		v.push_back(pii(i, num));
	}
	sort(v.begin(), v.end(), comp_ability);
	
	for (int i = 0; i < N; i++) {
		v[i].second = i;
	}
	
	sort(v.begin(), v.end(), comp_index);
	
	int h = (int)ceil(log2(N));
	int tree_size = 1 << (h + 1);
	Segment_tree sgt(tree_size);
	
	for (int i = 0; i < N; i++) {
		int front_num = 0;
		front_num = sgt.query(1, 0, N - 1, 0, v[i].second);
		cout << front_num + 1 << "\n";
		sgt.update(1, 0, N - 1, v[i].second, 1);
	}
	
	
	
	
	
	
	
	return 0;
} 
