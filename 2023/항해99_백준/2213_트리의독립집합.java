//트리의 독립집합 문제. 사실 '원자의 에너지'란 문제를 풀다가 이게 트리DP 유형이란 것을 보고 도저히 이해를 못하겠어서 근본 문제를 푸는게 좋을 것 같아 시작했다.
//https://loosie.tistory.com/223
//개인적으로 참고하며 너무 도움이 되었던 블로그이다.
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class Main {

  private ArrayList<Integer>[] list;
  private int[] w;
  private int[][] node;
  private boolean[] visit;
  private ArrayList<Integer> answer;

  public void solution() throws IOException {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int n = Integer.parseInt(br.readLine());
    w = new int[n + 1];
    StringTokenizer st = new StringTokenizer(br.readLine());
    for (int i = 1; i < n + 1; i++) {
      w[i] = Integer.parseInt(st.nextToken());
    }
    list = new ArrayList[n + 1];
    for (int i = 0; i < n + 1; i++) {
      list[i] = new ArrayList<>();
    }
    for (int i = 0; i < n - 1; i++) {
      st = new StringTokenizer(br.readLine());
      int a = Integer.parseInt(st.nextToken());
      int b = Integer.parseInt(st.nextToken());
      list[a].add(b);
      list[b].add(a);
    }

    node = new int[n + 1][2];
    visit = new boolean[n + 1];
    traversal(1);

    answer = new ArrayList<>();
    if (node[1][1] > node[1][0]) {
      System.out.println(node[1][1]);
      trace(1, 1);
    } else {
      System.out.println(node[1][0]);
      trace(1, 0);
    }

    Collections.sort(answer);
    for (int num : answer) {
      System.out.print(num + " ");
    }
  }

  public void traversal(int cur) {
    int childSize = list[cur].size();
    node[cur][0] = 0;
    node[cur][1] = w[cur];

    if (childSize == 0) return;

    visit[cur] = true;
    for (int child : list[cur]) {
      if (!visit[child]) {
        traversal(child);
        //현재 노드가 참석하지 않는 경우
        if (node[child][0] > node[child][1]) node[cur][0] += node[child][0];
        else node[cur][0] += node[child][1];
        //현재 노드가 참석하는 경우
        node[cur][1] += node[child][0];
      }
    }
    visit[cur] = false;
  }

  public void trace(int cur, int attend) {
    visit[cur] = true;
    if (attend == 1) {
      answer.add(cur);
      for (int i = 0; i < list[cur].size(); i++) {
        int next = list[cur].get(i);
        if (!visit[next]) {
          trace(next, 0);
        }
      }
    } else {
      for (int i = 0; i < list[cur].size(); i++) {
        int next = list[cur].get(i);
        if (!visit[next]) {
          if (node[next][1] > node[next][0]) trace(next, 1);
          else trace(next, 0);
        }
      }
    }
    visit[cur] = false;
  }

  public static void main(String[] args) throws IOException {
    new Main().solution();
  }

}