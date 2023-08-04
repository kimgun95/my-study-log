import java.io.*;
import java.util.*;

public class Main {

  private boolean[] visit;
  private boolean[] newVisit;
  private int[] distance;
  private int[] before;
  private ArrayList<Node>[] nodes;
  private int start;
  private int end;
  private int n;
  private int m;

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
    st = new StringTokenizer(br.readLine());
    start = Integer.parseInt(st.nextToken());
    end = Integer.parseInt(st.nextToken());

    visit = new boolean[n + 1];
    distance = new int[n + 1];
    before = new int[n + 1];
    for (int i = 1; i <= n; i++) {
      distance[i] = -1;
      before[i] = -1;
    }

    distance[start] = 0;
    int answer = 0;
    // 다익스트라 탐색 : 목적지 까지 최소 길이 탐색
    dijkstra(start);
    answer += distance[end];
    System.out.println("distane: " + distance[end]);

    newVisit = new boolean[n + 1];
    Stack<Integer> stack = new Stack<>();
    stack.add(before[end]);
    while (!stack.isEmpty()) {
      int node = stack.pop();
      newVisit[node] = true;
      if (before[node] == -1) break;
      stack.add(before[node]);
      System.out.println(node);
    }

    distance[start] = -1;
    visit = newVisit;
    visit[start] = false;
    dijkstra(end);
    answer += distance[start];
    System.out.println("distane: " + distance[start]);
    System.out.println(answer);
  }

  public void dijkstra(int node) {
    visit[node] = true;
    for (int i = 0; i < nodes[node].size(); i++) {
      Node to = nodes[node].get(i);
      if (visit[to.target]) continue;
      if (distance[to.target] == -1) {
        distance[to.target] = distance[node] + to.cost;
        before[to.target] = node;
      } else {
        if (distance[to.target] > distance[node] + to.cost) {
          distance[to.target] = distance[node] + to.cost;
          before[to.target] = node;
        }
      }
    }
    int minDist = Integer.MAX_VALUE;
    int idx = -1;
    for (int i = 1; i <= n; i++) {
      if (!visit[i] && distance[i] != -1)
        if (minDist > distance[i]) {
          minDist = distance[i];
          idx = i;
        }
    }
    if (idx != -1)
      dijkstra(idx);
  }

  public class Node {
    private int target;
    private int cost;

    public Node(int target, int cost) {
      this.target = target;
      this.cost = cost;
    }
  }


  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}