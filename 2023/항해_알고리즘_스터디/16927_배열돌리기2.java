// 큐빙이란 플레티넘 문제에서 좀 낮에 얻어 맞아서 그런지 집중해서 구현해서 풀어보았다.
// 1번에 solve!!!
import java.io.*;
import java.util.*;

public class Main {

  private int[][] board;
  private int r;
  private int n;
  private int m;

  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    n = Integer.parseInt(st.nextToken());
    m = Integer.parseInt(st.nextToken());
    r = Integer.parseInt(st.nextToken());
    board = new int[n][m];
    for (int i = 0; i < n; i++) {
      st = new StringTokenizer(br.readLine());
      for (int j = 0; j < m; j++) {
        board[i][j] = Integer.parseInt(st.nextToken());
      }
    }

    int size = Math.min(n, m) / 2;
    // 회전하는 써클 수
    for (int i = 0; i < size; i++) {
      // i, i 좌표를 시작점으로 하나의 써클
      rotate(i, i);
    }

    StringBuilder sb = new StringBuilder();
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
        sb.append(board[i][j]);
        if (j == m - 1) {
          sb.append("\n");
        } else {
          sb.append(" ");
        }
      }
    }
    System.out.println(sb);
  }

  private void rotate(int y, int x) {
    // 써클의 가로, 세로 길이
    int h = n - 2 * y;
    int w = m - 2 * x;
    int totalLength = 2 * h + 2 * w - 4; // 써클 둘레 길이
    int newR = r % totalLength; // 돌려야 하는 최적의 회전수

    for (int i = 0; i < newR; i++) {
      int temp = board[y][x];
      for (int j = y; j < y + h; j++) { // 윗줄, 오른쪽줄 회전하기
        for (int k = x; k < x + w; k++) {
          if (j == y) { // 윗줄 이동
            if (k != x + w - 1) {
              board[j][k] = board[j][k + 1];
            } else {
              board[j][k] = board[j + 1][k];
            }
          } else if (j != y + h - 1) { // 오른쪽줄 이동
            if (k == x + w - 1) {
              board[j][k] = board[j + 1][k];
            }
          }
        }
      }
      for (int j = y + h - 1; j >= y; j--) { // 아랫줄, 왼쪽줄 회전하기
        for (int k = x + w - 1; k >= x; k--) {
          if (j == y + h - 1) { // 아랫줄 이동
            if (k != x) {
              board[j][k] = board[j][k - 1];
            } else {
              if (h == 2) {
                board[j][k] = temp;
              } else {
                board[j][k] = board[j - 1][k];
              }
            }
          } else if (j != y) { // 왼쪽줄 이동
            if (k == x) {
              if (j == y + 1) {
                board[j][k] = temp;
              } else {
                board[j][k] = board[j - 1][k];
              }
            }
          }
        }
      }
    }

  }


  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}