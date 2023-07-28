// 내 예전 풀이를 봤는데 괜찮은데..?
import java.io.*;
import java.util.*;

public class Main {

  private int[][] board;
  private int n;
  private int answer;

  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    n = Integer.parseInt(br.readLine());

    board = new int[n][n];
    StringTokenizer st;
    for (int i = 0; i < n; i++) {
      st = new StringTokenizer(br.readLine());
      for (int j = 0; j < n; j++) {
        board[i][j] = Integer.parseInt(st.nextToken());
      }
    }
    answer = 0;
    // 0: 가로, 1: 세로, 2: 대각선
    findRoute(0, 1, 0);

    System.out.println(answer);
  }

  private void findRoute(int y, int x, int dir) {
    if (y >= n || x >= n || board[y][x] == 1) { // 해당 좌표에 놓을 수 있는지 판별
      return;
    }

    if (y == n - 1 && x == n - 1) { // 도착지점에 왔다면 카운트
      answer++;
      return;
    }

    if (dir != 0) { // 세로 방향
      findRoute(y + 1, x, 1);
    }
    if (dir != 1) { // 가로 방향
      findRoute(y, x + 1, 0);
    }
    // 대각선 방향
    if (y + 1 < n && x + 1 < n && board[y + 1][x] == 0 && board[y][x + 1] == 0) {
      findRoute(y + 1, x + 1, 2);
    }

  }

  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}