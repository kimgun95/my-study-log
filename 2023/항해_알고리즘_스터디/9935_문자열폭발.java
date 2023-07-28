// 문자열의 최대길이가 상당한 만큼 새롭게 String 할당을 여러번 시도하면 메모리 초과가 발생
// stack을 이용해 메모리의 사용을 최소화하고 문제 해결을 해야 함
// stack의 index 접근이 가능한줄 처음 알았음
import java.io.*;
import java.util.*;

public class Main {

  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    String str = br.readLine();
    String bomb = br.readLine();
    int bombLength = bomb.length();

    Stack<Character> stack = new Stack<>();
    for (int i = 0; i < str.length(); i++) { // stack에 문자하나씩 넣기
      stack.push(str.charAt(i));
      if (stack.size() >= bombLength) { // 문자열이 최상단에 완성되었는지 확인
        boolean check = true;
        for (int j = 0; j < bombLength; j++) {
          if (stack.get(stack.size() - bombLength + j) != bomb.charAt(j)) { // 만족하지 않는 문자열이라면 break
            check = false;
            break;
          }
        }
        if (check) { // 일치한다면 문자열 pop
          for (int j = 0; j < bombLength; j++) {
            stack.pop();
          }
        }
      }
    }

    StringBuilder answer = new StringBuilder();
    for (Character ch : stack) {
      answer.append(ch);
    }

    if (answer.length() == 0) {
      System.out.println("FRULA");
    } else System.out.println(answer);
  }


  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}