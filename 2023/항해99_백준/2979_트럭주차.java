import java.util.*;
import java.io.*;

public class Main {

  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    int a = Integer.parseInt(st.nextToken());
    int b = Integer.parseInt(st.nextToken());
    int c = Integer.parseInt(st.nextToken());
    int[] time = new int[101];
    for (int i = 0; i < 3; i++) {
      st = new StringTokenizer(br.readLine());
      int start = Integer.parseInt(st.nextToken());
      int end = Integer.parseInt(st.nextToken());
      for (int j = start; j < end; j++) {
        time[j]++;
      }
    }

    int answer = 0;
    for (int i = 1; i < 101; i++) {
      if (time[i] == 0) continue;
      else if (time[i] == 1) answer += a;
      else if (time[i] == 2) answer += b * 2;
      else if (time[i] == 3) answer += c * 3;
    }
    System.out.println(answer);
  }

  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}