// 벌써 3번째 풀이. 이젠 답을 외워버린 수준이다. ㅋㅋㅋㅋ
import java.util.*;
import java.io.*;

public class Main {


    private int answer;
    private boolean[][] visit;
    private int[][] board;
    private int n;
    private int m;

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        board = new int[n][m];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        visit = new boolean[n][m];
        answer = 0;
        // n,m의 최댓값이 500이라 모든 좌표에 대한 완전 탐색을 해도 부담이 없다.
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                visit[i][j] = true;
                dfs(i, j, 1, board[i][j]); // 4개의 칸 이동을 한다고 생각하며 dfs 탐색
                visit[i][j] = false;
            }
        }

        System.out.println(answer);
    }

    static int[][] dir = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

    // 해당 좌표(y, x)까지 진행하면서 몇 개(depth)를 이동했고 총 합(total)이 얼마인지
    private void dfs(int y, int x, int depth, int total) {
        if (depth == 4) { // 4칸 이동했다면 정답 갱신 시도
            answer = Math.max(answer, total);
            return;
        }

        for (int i = 0; i < 4; i++) { // 상하좌우 이동
            int ny = y + dir[i][0];
            int nx = x + dir[i][1];
            if (ny >= 0 && ny < n && nx >= 0 && nx < m && !visit[ny][nx]) {
                visit[ny][nx] = true;
                dfs(ny, nx, depth + 1, total + board[ny][nx]);
                // 'ㅗ'모양의 테트로미노를 만들기 위해선 3번째 칸 탐색 후 이전 칸에서 다시 탐색을 하면 된다.
                if (depth == 2) dfs(y, x, depth + 1, total + board[ny][nx]);
                visit[ny][nx] = false;
            }
        }
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}