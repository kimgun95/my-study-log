// 보자마자 Trie가 생각났다. 역시나 유형을 보니 Trie가 있었고 어느 정도 종이로 아이디어를 적은 후 확인차 예전 코드를 참고했다.
// 잊고 있었던 isLastChar를 알게 되었고 이전에 computeIfAbsent를 이용해 구현했던 것을 내 방식대로 getOrDefault로 변경하여 구현했다.
import java.io.*;
import java.util.*;


public class Main {

  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int t = Integer.parseInt(br.readLine());

    for (int i = 0; i < t; i++) {
      int n = Integer.parseInt(br.readLine());
      String[] numbers = new String[n];
      Trie trie = new Trie();
      for (int j = 0; j < n; j++) {
        numbers[j] = br.readLine();
        trie.insert(numbers[j]);
      }

      boolean answer = true;
      for (int j = 0; j < n; j++) {
        if (!trie.check(numbers[j])) {
          answer = false;
          break;
        }
      }
      if (answer) {
        System.out.println("YES");
      } else
        System.out.println("NO");
    }
  }

  public class Trie {
    private TrieNode rootNode;

    public Trie() {
      this.rootNode = new TrieNode();
    }

    public void insert(String str) {
      TrieNode thisNode = rootNode;
      for (int i = 0; i < str.length(); i++) {
        char ch = str.charAt(i);
        TrieNode targetNode = thisNode.getChildNodes().getOrDefault(ch, new TrieNode());
        thisNode.getChildNodes().put(ch, targetNode);
        thisNode = targetNode;
      }

      thisNode.isLastChar = true;
    }

    public boolean check(String str) {
      TrieNode thisNode = rootNode;
      for (int i = 0; i < str.length(); i++) {
        char ch = str.charAt(i);
        thisNode = thisNode.getChildNodes().get(ch);
        // System.out.println(ch);
        if (i < str.length() - 1 && thisNode.isLastChar) {
          return false;
        }
      }

      return true;
    }

  }

  public class TrieNode {
    private Map<Character, TrieNode> childNodes = new HashMap<>();
    private boolean isLastChar;

    public Map<Character, TrieNode> getChildNodes() {
      return childNodes;
    }

    public boolean isLastChar() {
      return isLastChar;
    }
  }


  public static void main(String[] args) throws Exception {

    new Main().solution();
  }

}