// 덱을 활용한 구현 문제이다.
// 문제에서 알려주는 흐름대로 구현하면 된다.
import java.io.*;
import java.util.*;

public class Main {

  private Deque<Integer> back;
  private Deque<Integer> front;
  private int current;
  private int[] arr;
  private int c;
  private int cache;

  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    int n = Integer.parseInt(st.nextToken());
    int q = Integer.parseInt(st.nextToken());
    c = Integer.parseInt(st.nextToken());

    // 각 페이지의 캐시 사이즈 저장
    arr = new int[n + 1];
    st = new StringTokenizer(br.readLine());
    for (int i = 1; i <= n; i++) {
      arr[i] = Integer.parseInt(st.nextToken());
    }

    back = new ArrayDeque<>();
    front = new ArrayDeque<>();
    current = -1;
    cache = 0;
    // 작업 시작
    for (int i = 0; i < q; i++) {
      st = new StringTokenizer(br.readLine());
      String op = st.nextToken();
      if (op.equals("A")) {
        int page = Integer.parseInt(st.nextToken());
        connect(page);
      } else if (op.equals("B")) {
        backTo();
      } else if (op.equals("F")) {
        frontTo();
      } else if (op.equals("C")) {
        compress();
      }
    }

    StringBuilder sb = new StringBuilder();
    sb.append(current).append("\n");
    if (back.isEmpty()) {
      sb.append(-1);
    } else {
      while (!back.isEmpty()) {
        sb.append(back.pollLast()).append(" ");
      }
    }
    sb.append("\n");
    if (front.isEmpty()) {
      sb.append(-1);
    } else {
      while (!front.isEmpty()) {
        sb.append(front.pollLast()).append(" ");
      }
    }
    System.out.println(sb);
  }

  private void connect(int page) {
    // 앞으로 가기 공간에 저장된 페이지 모두 삭제
    while (!front.isEmpty()) {
      int frontPage = front.pollFirst();
      cache -= arr[frontPage];
    }
    // 현재 페이지를 뒤로 가기 공간에 추가
    if (current != -1) {
      back.add(current);
    }
    current = page;
    cache += arr[page];
    // 첫 방문이 아니라면 뒤로 가기 공간에 추가하기
    while (cache > c) {
      int oldPage = back.pollFirst();
      cache -= arr[oldPage];
    }
  }

  private void backTo() {
    // 뒤로 가기 공간에 페이지가 있는 경우에만 실행
    if (back.size() > 0) {
      front.add(current);
      int backPage = back.pollLast();
      current = backPage;
    }
  }

  private void frontTo() {
    // 앞으로 가기 공간에 페이지가 있는 경우에만 실행
    if (front.size() > 0) {
      back.add(current);
      int frontPage = front.pollLast();
      current = frontPage;
    }
  }

  private void compress() {
    Deque<Integer> newBack = new ArrayDeque<>();
    int beforePage = -1;
    while (!back.isEmpty()) {
      int page = back.pollFirst();
      if (beforePage == page) {
        cache -= arr[page];
        continue;
      }
      beforePage = page;
      newBack.add(page);
    }
    back = newBack;
  }

  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}