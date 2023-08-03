// dp를 바로 직감했지만 흑,백의 갯수를 어떻게 표현하여 해결해야할지 몰랐음
import java.io.*;
import java.util.*;

public class Main {

  private int size;
  private int[][][] dp;
  private int[] white;
  private int[] black;

  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    String input = "";
    // 흑,백의 갯수를 dp의 배열로 표현하는 아이디어를 떠올릴 수가 없었음
    dp = new int[1001][16][16];
    // 몇 개를 입력값으로 받을지 모르기 때문에 최대 1000 사이즈로 설정한다.
    white = new int[1001];
    black = new int[1001];

    int idx = 1;
    StringTokenizer st;
    // EOF에 대비한 입력값 받기
    while ((input = br.readLine()) != null && !input.isEmpty()) {
      st = new StringTokenizer(input);
      white[idx] = Integer.parseInt(st.nextToken());
      black[idx] = Integer.parseInt(st.nextToken());
      idx++;
    }
    size = idx; // 팀원의 총 숫자

    int answer = dfs(0, 0, 0);

    System.out.println(answer);
  }

  private int dfs(int index, int countWhite, int countBlack) {
    // 인원을 포함시킬 때 마다 값은 더해지기 때문에 조건이 만족하는 순간은 0 값을 리턴한다.
    if (countWhite == 15 && countBlack == 15) return 0;
    if (index == size) return 0;
    if (dp[index][countWhite][countBlack] != 0)
      return dp[index][countWhite][countBlack];

    // 선택하지 않는 경우
    int result = dfs(index + 1, countWhite, countBlack);
    if (countWhite < 15)
      result = Math.max(result, dfs(index + 1, countWhite + 1, countBlack) + white[index]);
    if (countBlack < 15)
      result = Math.max(result, dfs(index + 1, countWhite, countBlack + 1) + black[index]);

    dp[index][countWhite][countBlack] = result;
    return dp[index][countWhite][countBlack];
  }


  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}