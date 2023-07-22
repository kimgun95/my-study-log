// dp 범위 정하기에서 오래 걸림. 그냥 1000(c 최댓값) + 100(n 최댓값) + 1 로 설정함
import java.io.*;
import java.util.*;

public class Main {

  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    int c = Integer.parseInt(st.nextToken());
    int n = Integer.parseInt(st.nextToken());


    ArrayList<AD> ads = new ArrayList<>();
    for (int i = 0; i < n; i++) {
      st = new StringTokenizer(br.readLine());
      int cost = Integer.parseInt(st.nextToken());
      int people = Integer.parseInt(st.nextToken());
      ads.add(new AD(people, cost));
    }

    // dp 초기화
    int[] dp = new int[1101];
    int len = ads.size();
    for (int i = 0; i < len; i++) {
      AD ad = ads.get(i);
      if (dp[ad.people] != 0) {
        dp[ad.people] = Math.min(dp[ad.people], ad.cost);
      } else {
        dp[ad.people] = ad.cost;
      }
    }

    for (int i = 1; i < c; i++) {
      for (int j = 0; j < len; j++) {
        int people = i + ads.get(j).people;
        if (dp[i] != 0 && people < dp.length) {
          int cost = dp[i] + ads.get(j).cost;
          if (dp[people] != 0) {
            dp[people] = Math.min(dp[people], cost);
          } else {
            dp[people] = cost;
          }
        }
      }
    }

    int answer = Integer.MAX_VALUE;
    for (int i = c; i < dp.length; i++) {
      if (dp[i] != 0) {
        answer = Math.min(answer, dp[i]);
      }
    }
    System.out.println(answer);
  }

  private class AD {
    private int people;
    private int cost;

    public AD(int people, int cost) {
      this.people = people;
      this.cost = cost;
    }
  }

  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}