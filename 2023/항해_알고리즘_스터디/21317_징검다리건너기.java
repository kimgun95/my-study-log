// dp 라는 배열을 정의해서 값을 갱신해야 된다는 생각에 사로잡혀 풀지 못했음
// 징검다리는 중간에 생략 없이 계속 걸어 나가야하는 거기 때문에 dfs로 풀면 되는 문제
import java.io.*;
import java.util.*;

public class Main {

  private int answer;
  private int n;
  private Energy[] energy;
  private int k;

  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    n = Integer.parseInt(br.readLine());
    energy = new Energy[n + 1];

    for (int i = 1; i <= n - 1; i++) {
      StringTokenizer st = new StringTokenizer(br.readLine());
      energy[i] = new Energy(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
    }
    k = Integer.parseInt(br.readLine());

    answer = Integer.MAX_VALUE;
    recursive(1, 0, 0);

    System.out.println(answer);
  }

  public void recursive(int target, int isUsed, int total) { // target 까지 total 만큼의 에너지가 소모되었음
    if (total >= answer) {
      return;
    }
    if (target > n) {
      return;
    }
    if (target == n) {
      answer = total;
      return;
    }

    recursive(target + 1, isUsed, total + energy[target].small);
    recursive(target + 2, isUsed, total + energy[target].big);
    if (isUsed == 0) {
      recursive(target + 3, 1, total + k);
    }
  }

  public class Energy {
    private int small;
    private int big;

    public Energy(int small, int big) {
      this.small = small;
      this.big = big;
    }
  }

  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}