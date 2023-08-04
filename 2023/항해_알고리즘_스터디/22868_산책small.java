// bfs를 이용, 그러나 경로를 저장해야 하는 문제
// 처음 리스트를 정렬도 해야 해서 신경써야할게 많다.
import java.util.*;
import java.io.*;

public class Main {


    private int n;
    private int m;
    private ArrayList<Integer>[] nodes;
    private int start;
    private int end;
    private boolean[] visit;
    private int[] beforeNode;
    private int answer;

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        nodes = new ArrayList[n + 1];
        for (int i = 1; i <= n; i++) {
            nodes[i] = new ArrayList<>();
        }
        for (int i = 1; i <= m; i++) { // 여기 m 값을 n으로 해놔서 개고생했다.
            st = new StringTokenizer(br.readLine());
            int nodeA = Integer.parseInt(st.nextToken());
            int nodeB = Integer.parseInt(st.nextToken());
            nodes[nodeA].add(nodeB);
            nodes[nodeB].add(nodeA);
        }

        st = new StringTokenizer(br.readLine());
        start = Integer.parseInt(st.nextToken());
        end = Integer.parseInt(st.nextToken());

        // 입력 받은 경로를 정렬한다 -> 사전순 경로를 찾는데 최적의 재료가 되기 때문
        for (int i = 1; i <= n; i++) {
            Collections.sort(nodes[i]);
        }

        answer = 0;
        // bfs로 최단 거리를 계산 (s -> e)
        visit = new boolean[n + 1];
        beforeNode = new int[n + 1];
        bfs(start, end);


        // 위에서 찾은 최단 경로를 체크하기 위해 새롭게 visit 정의
        for (int i = 1; i <= n; i++) {
            visit[i] = false;
        }
        int checkedNode = beforeNode[end];
        while (checkedNode > 0 && checkedNode != start) { // 출발지는 굳이 visit 처리하지 않는다.
            visit[checkedNode] = true;
            checkedNode = beforeNode[checkedNode];
        }

        // bfs로 최단 거리를 계산 (e -> s)
        bfs(end, start);

        System.out.println(answer);
    }

    private void bfs(int from, int to) {
        Deque<Info> dq = new ArrayDeque<>();
        dq.offer(new Info(from, 0));
        visit[from] = true;

        while (!dq.isEmpty()) {
            Info current = dq.pollFirst();
            for (int i = 0; i < nodes[current.node].size(); i++) {
                int target = nodes[current.node].get(i);
                if (visit[target]) continue;
                visit[target] = true;
                beforeNode[target] = current.node;
                dq.offer(new Info(target, current.depth + 1));

                if (target == to) { // 목적지에 도착했으면 bfs 종료
                    answer += current.depth + 1;
                    return;
                }

            }
        }
    }

    private class Info {
        private int node;
        private int depth;

        public Info(int node, int depth) {
            this.node = node;
            this.depth = depth;
        }
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}