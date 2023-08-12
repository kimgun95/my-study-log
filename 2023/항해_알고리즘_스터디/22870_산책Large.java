
import java.util.*;
import java.io.*;

public class Main {


    private int n;
    private int m;
    private ArrayList<Node>[] nodes;
    private int start;
    private int end;
    private boolean[] visit;
    private int[] beforeNode;
    private int[] distance;
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
        for (int i = 1; i <= m; i++) {
            st = new StringTokenizer(br.readLine());
            int nodeA = Integer.parseInt(st.nextToken());
            int nodeB = Integer.parseInt(st.nextToken());
            int cost = Integer.parseInt(st.nextToken());
            nodes[nodeA].add(new Node(nodeB, cost));
            nodes[nodeB].add(new Node(nodeA, cost));
        }

        st = new StringTokenizer(br.readLine());
        start = Integer.parseInt(st.nextToken());
        end = Integer.parseInt(st.nextToken());

        // 입력 받은 경로를 정렬한다 -> 사전순 경로를 찾는데 최적의 재료가 되기 때문
        for (int i = 1; i <= n; i++) {
            Collections.sort(nodes[i]);
        }

        answer = 0;
        // dijkstra 탐색 (s -> e)
        visit = new boolean[n + 1];
        beforeNode = new int[n + 1];
        distance = new int[n + 1];
        for (int i = 0; i < n + 1; i++) {
            distance[i] = Integer.MAX_VALUE;
        }
        dijkstra(start, end);
        answer += distance[end];
        System.out.println("end : " + distance[end]);

        // 위에서 찾은 최단 경로를 체크하기 위해 새롭게 visit 정의
        for (int i = 0; i <= n; i++) {
            visit[i] = false;
            distance[i] = Integer.MAX_VALUE;
        }
        int checkedNode = beforeNode[end];
        while (checkedNode > 0 && checkedNode != start) {
            visit[checkedNode] = true;
            System.out.println(checkedNode);
            checkedNode = beforeNode[checkedNode];
        }
        System.out.println("---------------");
        // dijkstra 최단 거리를 계산 (e -> s)
        dijkstra(end, start);
        answer += distance[start];
        System.out.println("start : " + distance[start]);
        checkedNode = beforeNode[start];
        while (checkedNode > 0 && checkedNode != end) {
            visit[checkedNode] = true;
            System.out.println(checkedNode);
            checkedNode = beforeNode[checkedNode];
        }

        System.out.println(answer);
    }

    private void dijkstra(int from, int to) {
        distance[from] = 0;
        PriorityQueue<Info> pq = new PriorityQueue<>();
        pq.add(new Info(from, 0, 0));

        while (!pq.isEmpty()) {
            Info info = pq.poll();
            if (visit[info.node]) continue;
            visit[info.node] = true;

            if (info.node == to) break;

            for (int i = 0; i < nodes[info.node].size(); i++) {
                Node target = nodes[info.node].get(i);
                if (distance[target.node] > distance[info.node] + target.cost) {
                    distance[target.node] = distance[info.node] + target.cost;
                    beforeNode[target.node] = info.node;
                    pq.add(new Info(target.node, info.depth + 1, distance[target.node]));
                }
            }
        }

    }

    private class Node implements Comparable<Node> {
        private int node;
        private int cost;

        public Node(int node, int cost) {
            this.node = node;
            this.cost = cost;
        }

        @Override
        public int compareTo(Node o) {
            return this.node - o.node;
        }
    }

    private class Info implements Comparable<Info> {
        private int node;
        private int depth;
        private int total;

        public Info(int node, int depth, int total) {
            this.node = node;
            this.depth = depth;
            this.total = total;
        }

        @Override
        public int compareTo(Info o) {
            if (this.total != o.total) {
                return this.total - o.total;
            }
            return this.node - o.node;
        }
    }



    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}