// 처음에 우선순위큐를 사용하지 않고 직접 탐색할 다음 노드를 찾는 방식으로 구현했음 -> 시간초과 발생
// 우선순위큐의 특성을 이용해 정렬된 값을 가져오는 방식. 이때 Comparable 인터페이스의 compareTo를 잘 정의해 사용한다.
import java.util.*;
import java.io.*;

public class Main {


    private ArrayList<Node>[] nodes;
    private int n;
    private int m;
    private boolean[] visit;
    private int[] answer;

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        nodes = new ArrayList[n + 1];
        for (int i = 1; i <= n; i++) {
            nodes[i] = new ArrayList<>();
        }
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int nodeA = Integer.parseInt(st.nextToken());
            int nodeB = Integer.parseInt(st.nextToken());
            int cost = Integer.parseInt(st.nextToken());
            nodes[nodeA].add(new Node(nodeB, cost));
            nodes[nodeB].add(new Node(nodeA, cost));
        }

        visit = new boolean[n + 1]; // 방문 여부 체크
        answer = new int[n + 1]; // 노드마다 최적의 비용 저장
        for (int i = 1; i <= n; i++) {
            answer[i] = Integer.MAX_VALUE;
        }
        answer[1] = 0; // 시작 노드의 비용은 0으로 설정
        // 다익스트라 탐색
        dijkstra(1);

        System.out.println(answer[n]);
    }

    private void dijkstra(int node) {
        // 우선순위큐는 탐색할 다음 노드를 편하게 꺼내기 위해 사용
        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.offer(new Node(1, 0));

        while (!pq.isEmpty()) {
            Node from = pq.poll();
            // 방문했던 노드는 탐색하지 않는다.
            if (visit[from.dest]) continue;
            visit[from.dest] = true;

            for (int i = 0; i < nodes[from.dest].size(); i++) { // 노드와 연결된 경로를 통해 도착 노드의 값을 갱신
                Node to = nodes[from.dest].get(i);
                int cost = answer[from.dest] + to.cost;
                if (cost < answer[to.dest]) {
                    answer[to.dest] = cost;
                    pq.offer(new Node(to.dest, answer[to.dest]));
                }
            }
        }
    }

    // Comparable 인터페이스를 상속 받아 compareTo 오버라이드를 통해 우선순위큐 정렬에 적용한다.
    private class Node implements Comparable<Node> {
        private int dest;
        private int cost;

        public Node(int dest, int cost) {
            this.dest = dest;
            this.cost = cost;
        }

        @Override
        public int compareTo(Node node) {
            return this.cost - node.cost;
        }
    }


    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}