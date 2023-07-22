// bfs 탐색. visit 위치 잘 선정하기. get이 아닌 pollFirst로 사용하기
import java.io.*;
import java.util.*;

public class Main {

  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    int w = Integer.parseInt(st.nextToken());
    int h = Integer.parseInt(st.nextToken());
    int n = Integer.parseInt(br.readLine());
    int[][] board = new int[h][w];
    boolean[][] visit = new boolean[h][w];
    Deque<Node> dq = new ArrayDeque<>();
    int totalLamp = 0;

    // block: 1, dust: 2, lamp: 3
    for (int i = 0; i < n; i++) {
      st = new StringTokenizer(br.readLine());
      String str = st.nextToken();
      int x = Integer.parseInt(st.nextToken());
      int y = Integer.parseInt(st.nextToken());
      if (str.equals("redstone_block")) { // 전기신호 15 전달
        board[y][x] = 1;
        dq.add(new Node(y, x, 16));
        visit[y][x] = true;
      } else if (str.equals("redstone_dust")) { // 전기신호 전이
        board[y][x] = 2;
      } else if (str.equals("redstone_lamp")) { // 불 on/off
        board[y][x] = 3;
        totalLamp++;
      }
    }

    int[][] dir = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    int count = 0; // 불 키는 lamp 수를 카운트

    // bfs 탐색
    while (!dq.isEmpty()) {
      Node node = dq.pollFirst();

      for (int i = 0; i < 4; i++) {
        int ny = node.y + dir[i][0];
        int nx = node.x + dir[i][1];
        if (ny >= 0 && ny < h && nx >= 0 && nx < w && !visit[ny][nx] && node.energy > 1) {
          if (board[ny][nx] == 3) { // lamp 불 키기
            visit[ny][nx] = true;
            count++;
          } else if (board[ny][nx] == 2) { // 전기 신호 전이
            visit[ny][nx] = true;
            dq.add(new Node(ny, nx, node.energy - 1));
          }
        }
      }
    }

    if (count == totalLamp) { // 모든 램프를 켰다면
      System.out.println("success");
    } else {
      System.out.println("failed");
    }
  }

  private class Node {
    private int y;
    private int x;
    private int energy;

    public Node(int y, int x, int energy) {
      this.y = y;
      this.x = x;
      this.energy = energy;
    }
  }


  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}