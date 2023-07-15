// 시간 초과 발생 문제. 처음에는 해당 숫자를 사용하느냐, 사용하지 않느냐로 dfs 탐색을 했음
// 순환하는 흐름을 찾으면 되는 문제. start, target 을 두고 처음부터 끝으로 순환 고리가 만들어지는지 dfs 탐색을 하는 것
import java.io.*;
import java.util.*;

public class Main {

  private int n;
  private int[] board;
  private boolean[] visit;
  private List<Integer> answer;

  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    n = Integer.parseInt(br.readLine());

    board = new int[n + 1];
    for (int i = 1; i <= n; i++) {
      int num = Integer.parseInt(br.readLine());
      board[i] = num;
    }

    answer = new ArrayList<>(); // 순환을 만들어내는 숫자가 하나씩 추가될 list
    visit = new boolean[n + 1];
    for (int i = 1; i <= n; i++) {
      visit[i] = true;
      dfs(i, i); // 결국 자기 자신으로 돌아와야 순환되는 것
      visit[i] = false;
    }

    Collections.sort(answer); // Collections을 이용한 sort
    StringBuilder sb = new StringBuilder();
    sb.append(answer.size()).append("\n");
    for (int i = 0; i < answer.size(); i++) {
      sb.append(answer.get(i)).append("\n");
    }
    System.out.println(sb);
  }

  public void dfs(int start, int target) {
    if (board[start] == target) {
      answer.add(target); // 순환에 성공했다면 이 target 숫자는 결국 순환 흐름 중 하나의 요소가 되는 것이므로 list에 추가
    }
    if (!visit[board[start]]) {
      visit[board[start]] = true;
      dfs(board[start], target);
      visit[board[start]] = false;
    }
  }

  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}