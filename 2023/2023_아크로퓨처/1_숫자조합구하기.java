import java.util.*;

public class Main {

  private String[] strings;
  private boolean[] visit;
  private Stack<String> stack;
  private String answer;

  public String solution1(int[] numbers) throws Exception {

    strings = new String[numbers.length];
    for (int i = 0; i < numbers.length; i++) {
      strings[i] = String.valueOf(numbers[i]);
    }

    Arrays.sort(strings);
    visit = new boolean[numbers.length];
    stack = new Stack<>();
    answer = "";
    for (int i = 0; i < numbers.length; i++) {
      visit[i] = true;
      stack.push(strings[i]);
      dfs(1);
      stack.pop();
      visit[i] = false;
    }

    return answer;
  }

  public void dfs(int count) {
    if (count == strings.length) {
      StringBuilder newStr = new StringBuilder();
      for (String str : stack) {
        newStr.append(str);
      }
      if (answer.equals("") || answer.compareTo(newStr.toString()) > 0) {
        answer = newStr.toString();
      }
      return;
    }
    for (int i = 0; i < strings.length; i++) {
      if (visit[i]) continue;
      String top = stack.peek();
      if (top.charAt(0) > strings[i].charAt(0)) return;
      visit[i] = true;
      stack.push(strings[i]);
      dfs(count + 1);
      stack.pop();
      visit[i] = false;
    }
  }


  public static void main(String[] args) throws Exception {
    int[] numbers = {11, 6, 10, 0};
    new Main().solution1(numbers);
  }

}