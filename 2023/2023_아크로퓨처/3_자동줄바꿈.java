import java.util.*;


public class Main {

  public String solution3(String text, int n) throws Exception {

    ArrayList<String> list = new ArrayList<>();
    int beforeIdx = 0;
    int currentIdx = 0;
    int size = 0;
    while (currentIdx < text.length()) {
      if (size == 18) {
        if (currentIdx + 1 < text.length() && isKorean(text.charAt(currentIdx + 1)) == 2) {
          currentIdx++;
          list.add(text.substring(beforeIdx, currentIdx));
          beforeIdx = currentIdx;
          size = 0;
          continue;
        } else if (currentIdx + 1 < text.length() && isKorean(text.charAt(currentIdx + 1)) == 1) {
          currentIdx++;
          size++;
          continue;
        }
      } else if (size == 19) {
        if (currentIdx + 1 < text.length() && isKorean(text.charAt(currentIdx + 1)) == 2) {
          currentIdx++;
          list.add(text.substring(beforeIdx, currentIdx));
          beforeIdx = currentIdx;
          size = 0;
          continue;
        } else if (currentIdx + 1 < text.length() && isKorean(text.charAt(currentIdx + 1)) == 1) {
          currentIdx++;
          list.add(text.substring(beforeIdx, currentIdx));
          beforeIdx = currentIdx;
          size = 0;
          continue;
        }
      }

      if (isKorean(text.charAt(currentIdx)) == 1) size++;
      else size += 2;
      currentIdx++;
    }

    list.add(text.substring(beforeIdx, currentIdx));

    for (String str : list) {
      System.out.println(str);
    }

    return "";
  }

  public int isKorean(char ch) {
    if ((ch >= 'a' && ch <= 'z') || (ch >= 'A' && ch <= 'Z') || (ch >= '0' && ch <= '9')) {
      return 1;
    }
    return 2;
  }


  public static void main(String[] args) throws Exception {
    String str = "가나다abc123가나다abc123가나다abc123가나다abc123가나다abc123가나다abc123가나다abc123가나다abc123";
    int n = 20;
    new Main().solution3(str, n);
  }

}