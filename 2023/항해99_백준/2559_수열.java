import java.util.*;
import java.io.*;

public class Main {

  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    int n = Integer.parseInt(st.nextToken());
    int k = Integer.parseInt(st.nextToken());
    int[] temperature = new int[n];
    st = new StringTokenizer(br.readLine());
    for (int i = 0; i < n; i++) {
      temperature[i] = Integer.parseInt(st.nextToken());
    }
    int answer = Integer.MIN_VALUE;
    for (int i = 0; i < n - k + 1; i++) {
      int result = 0;
      for (int j = i; j < i + k; j++) {
        result += temperature[j];
      }
      answer = Math.max(answer, result);
    }
    System.out.println(answer);

  }

  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}