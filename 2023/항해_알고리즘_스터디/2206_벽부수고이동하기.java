// 처음에 dp로 풀어보려고 했다. 그러나 그래프 탐색을 이용하지 않으면 경로 탐색이 불가함을 깨닫았다.
// dp로 정의한 자료구조를 visit으로 정의하여 풀어야 했다.
// 따라서 그래프 탐색은 두 가지 경우가 동시에 진행된다. 벽을 부쉈는지 안부쉈는지
// 그에 따라 visit[][][0] 과 visit[][][1]로 나누어 체크를 하게 된다.
import java.io.*;
import java.util.*;


public class Main {

  private int n;
  private int m;

  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    n = Integer.parseInt(st.nextToken());
    m = Integer.parseInt(st.nextToken());
    char[][] board = new char[n][m];
    for (int i = 0; i < n; i++) {
      String input = br.readLine();
      for (int j = 0; j < m; j++) {
        board[i][j] = input.charAt(j);
      }
    }

    int[][] dir = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    Queue<Location> q = new ArrayDeque<>();
    q.add(new Location(0, 0, 1, false));
    boolean[][][] visit = new boolean[n][m][2];

    while (!q.isEmpty()) {
      Location location = q.poll();
      if (location.y == n - 1 && location.x == m - 1) {
        System.out.println(location.cnt);
        return;
      }

      for (int i = 0; i < 4; i++) {
        int ny = location.y + dir[i][0];
        int nx = location.x + dir[i][1];
        if (ny < 0 || ny >= n || nx < 0 || nx >= m) continue;

        if (board[ny][nx] == '0') { // 진행하는 곳이 벽이 아니라면
          if (!location.destroyed && !visit[ny][nx][0]) { // 아직 벽을 부수지 않았고 진행한 곳 방문하지 않았을 때
            q.add(new Location(ny, nx, location.cnt + 1, false));
            visit[ny][nx][0] = true;
          } else if (location.destroyed && !visit[ny][nx][1]) { // 벽을 부쉈고 진행한 곳 방문하지 않았을 때
            q.add(new Location(ny, nx, location.cnt + 1, true));
            visit[ny][nx][1] = true;
          }
        } else { // 벽이라면
          if (!location.destroyed && !visit[ny][nx][1]) {
            q.add(new Location(ny, nx, location.cnt + 1, true));
            visit[ny][nx][1] = true;
          }
        }
      }
    }

    System.out.println(-1);

  }

  public class Location {
    int y;
    int x;
    int cnt;
    boolean destroyed;

    public Location(int y, int x, int cnt, boolean destroyed) {
      this.y = y;
      this.x = x;
      this.cnt = cnt;
      this.destroyed = destroyed;
    }
  }


  public static void main(String[] args) throws Exception {

    new Main().solution();
  }

}