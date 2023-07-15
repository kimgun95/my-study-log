// 시간 초과 발생. 단순하게 Comparator를 통해 계속 비교를 하며 진행했음.
// 우선 순위 큐를 이용해 후보를 넣고 빼고 하는 식으로 진행. 이때 Comparator 정의 필수.
import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

public class Main {



  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    int n = Integer.parseInt(st.nextToken());
    int m = Integer.parseInt(st.nextToken());
    int k = Integer.parseInt(st.nextToken());

    LinkedList<Person>[] lineList = new LinkedList[m];
    for (int i = 0; i < m; i++) {
      lineList[i] = new LinkedList<>();
    }

    // m개의 줄로 나눠 줄서기
    for (int i = 0; i < n; i++) {
      st = new StringTokenizer(br.readLine());
      int d = Integer.parseInt(st.nextToken());
      int h = Integer.parseInt(st.nextToken());

      lineList[i % m].add(new Person(d, h, i, i % m));
    }

    // 우선 순위 큐 정렬 정의하기
    PriorityQueue<Person> pq = new PriorityQueue<>(new Comparator<Person>() {
      @Override
      public int compare(Person o1, Person o2) {
        int d = o2.D - o1.D;
        if (d == 0) {
          int h = o2.H - o1.H;
          if (h == 0) {
            return o1.line - o2.line;
          }
          return h;
        }
        return d;
      }
    });

    for (int i = 0; i < m; i++) { // 각 줄의 선두를 후보로 넣기
      if (lineList[i].size() == 0) { // 이 줄 부터는 후보로 넣을 사람 없음
        break;
      }
      pq.add(lineList[i].remove(0));
    }

    // 내 번호는 k번째
    int count = 0;

    // 화장실 보내기 시작
    while (!pq.isEmpty()) {
      Person first = pq.poll(); // 최적의 후보 화장실 보내기
      if (first.getIndex() == k) { // 내 차례라면 break
        System.out.println(count);
        break;
      }
      count++;
      if (lineList[first.getLine()].size() != 0) { // 후보가 나간 줄에서 다음 후보를 추가
        pq.add(lineList[first.getLine()].remove(0));
      }
    }
  }

  public class Person {
    private int D;
    private int H;
    private int index;
    private int line;

    public Person(int d, int h, int index, int line) {
      D = d;
      H = h;
      this.index = index;
      this.line = line;
    }

    public int getD() {
      return D;
    }

    public int getH() {
      return H;
    }

    public int getIndex() {
      return index;
    }

    public int getLine() {
      return line;
    }
  }


  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}