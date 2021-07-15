// 6416 - 트리인가?
// 내가 풀었던 코드로도 50%까지 접근했었는데 왜 틀렸는지 이해가 가지 않는다... 뭐 되게 큰 값들을 못받아와서 그런건가..? 싶기도 하지만 모르겠다.
// 노드를 저장할때 배열을 이용해서 check했었는데 그냥 set을 이용해서 중복 노드는 알아서 저장 안되게 하는 이 사람의 풀이도 좋은 것 같다. 
#include <iostream>
#include <vector>
#include <set>
using namespace std;

typedef pair<int, int> pii;

int a, b; // 입력 변수 
int kase = 1;  // case 표현 수. 
vector<pii> v; // 간선 저장 벡터. 
set<int> s; // 노드 저장 set. 중복은 알아서 걸러주니 좋은 자료형. 

int main() {
	
	while(true) {
		cin >> a >> b;
		// 종료 조건. 
		if (a == -1 && b == -1) break;
		if (a == 0 && b == 0) {
			// 트리인지 검사.
			if (v.size() + 1 == s.size() || v.size() == 0) cout << "Case " << kase << " is a tree.\n";
			else cout << "Case " << kase << " is not a tree.\n";
			kase++;
			v.clear();
			s.clear();
		} else {
			// 노드 추가. 
			v.push_back(pii(a, b));
			s.insert(a);
			s.insert(b);
		}
	}	

	
	return 0;
} 
