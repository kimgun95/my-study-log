import java.util.*;
import java.io.*;

public class Main {

  private int n;
  private int m;
  private int[][] board;

  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    n = Integer.parseInt(st.nextToken());
    m = Integer.parseInt(st.nextToken());
    board = new int[n][m];
    for (int i = 0; i < n; i++) {
      String strInput = br.readLine();
      for (int j = 0; j < m; j++) {
        board[i][j] = strInput.charAt(j) - '0';
      }
    }

    int answer = bfs();
    System.out.println(answer);
  }

  int[][] dir = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
  public int bfs() {
    ArrayDeque<Coordinate> deque = new ArrayDeque<>();
    deque.add(new Coordinate(0, 0, 1));
    boolean[][] visit = new boolean[n][m];
    while (!deque.isEmpty()) {
      Coordinate c = deque.pollFirst();
      if (c.y == n - 1 && c.x == m - 1) return c.count;
      if (visit[c.y][c.x]) continue;
      visit[c.y][c.x] = true;
      for (int i = 0; i < 4; i++) {
        int ny = c.y + dir[i][0];
        int nx = c.x + dir[i][1];
        if (ny >= 0 && ny < n && nx >= 0 && nx < m && board[ny][nx] == 1) {
          deque.add(new Coordinate(ny, nx, c.count + 1));
        }
      }
    }
    return 0;
  }

  public class Coordinate {
    private int y;
    private int x;
    private int count;
    public Coordinate(int y, int x, int count) {
      this.y = y;
      this.x = x;
      this.count = count;
    }
  }


  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}