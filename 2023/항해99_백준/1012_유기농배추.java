import java.util.*;
import java.io.*;

public class Main {


  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int t = Integer.parseInt(br.readLine());
    StringBuilder sb = new StringBuilder();
    for (int i = 0; i < t; i++) {
      StringTokenizer st = new StringTokenizer(br.readLine());
      int m = Integer.parseInt(st.nextToken());
      int n = Integer.parseInt(st.nextToken());
      int k = Integer.parseInt(st.nextToken());
      int[][] board = new int[n][m];
      for (int j = 0; j < k; j++) {
        st = new StringTokenizer(br.readLine());
        int x = Integer.parseInt(st.nextToken());
        int y = Integer.parseInt(st.nextToken());
        board[y][x] = 1;
      }
      boolean[][] visit = new boolean[n][m];
      int[][] dir = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
      int result = 0;
      for (int j = 0; j < n; j++) {
        for (int l = 0; l < m; l++) {
          if (!visit[j][l] && board[j][l] == 1) {
            result++;
            Stack<Coordinate> stack = new Stack<>();
            stack.add(new Coordinate(j, l));
            while (!stack.isEmpty()) {
              Coordinate c = stack.pop();
              if (visit[c.y][c.x]) continue;
              visit[c.y][c.x] = true;
              for (int o = 0; o < 4; o++) {
                int ny = c.y + dir[o][0];
                int nx = c.x + dir[o][1];
                if (ny >= 0 && ny < n && nx >= 0 && nx < m && board[ny][nx] == 1) {
                  stack.push(new Coordinate(ny, nx));
                }
              }
            }
          }
        }
      }
      sb.append(result + "\n");
    }
    System.out.println(sb);
  }

  public class Coordinate {
    private int y;
    private int x;
    public Coordinate(int y, int x) {
      this.y = y;
      this.x = x;
    }
  }

  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}