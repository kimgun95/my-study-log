import java.util.*;
import java.io.*;

public class Main {

  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int n = Integer.parseInt(br.readLine());
    String[] words = new String[n];
    for (int i = 0; i < n; i++) {
      words[i] = br.readLine();
    }
    int answer = 0;
    for (String str : words) {
      if (check(str)) answer++;
    }

    System.out.println(answer);
  }

  public boolean check(String str) {
    Stack<Character> stack = new Stack<>();
    for (int i = 0; i < str.length(); i++) {
      char ch = str.charAt(i);
      if (!stack.empty()) {
        if (stack.peek() == ch) stack.pop();
        else stack.push(ch);
      } else stack.push(ch);
    }
    if (!stack.empty()) return false;
    return true;
  }

  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}