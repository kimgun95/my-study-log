// 처음 풀이를 할 때 끝난 강의를 모두 알아내는 코드를 작성했는데 '시간 초과'가 발생
// 굳이 다 알아내지 않고 끝나는 강의 하나만 있으면 그 강의실에 새로운 강의 추가
import java.io.*;
import java.util.*;

public class Main {


  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int n = Integer.parseInt(br.readLine());
    PriorityQueue<Lecture> lectures = new PriorityQueue<>();
    StringTokenizer st;
    for (int i = 0; i < n; i++) {
      st = new StringTokenizer(br.readLine());
      int num = Integer.parseInt(st.nextToken());
      int start = Integer.parseInt(st.nextToken());
      int end = Integer.parseInt(st.nextToken());
      lectures.add(new Lecture(num, start, end));
    }

    PriorityQueue<Room> rooms = new PriorityQueue<>();
    int answer = 0;
    int[] list = new int[n + 1];
    for (int i = 0; i < n; i++) {
      Lecture lecture = lectures.poll();
      // 강의가 끝난 곳에 새로 추가
      if (!rooms.isEmpty() && rooms.peek().end <= lecture.start) {
        Room room = rooms.poll();
        rooms.add(new Room(room.num, lecture.end));
        list[lecture.num] = room.num;
      } else { // 없다면 강의실 새로 추가
        answer++;
        rooms.add(new Room(answer, lecture.end));
        list[lecture.num] = answer;
      }
    }

    // 출력. 이때 강의 번호대로 해당 강의가 어떤 강의실에서 진행됐는지 출력
    StringBuilder sb = new StringBuilder();
    sb.append(answer).append("\n");
    for (int i = 1; i < list.length; i++) {
      sb.append(list[i]);
      if (i != list.length - 1)
        sb.append("\n");
    }
    System.out.println(sb);
  }

  public class Room implements Comparable<Room> {
    int num;
    int end;

    public Room(int num, int end) {
      this.num = num;
      this.end = end;
    }

    @Override
    public int compareTo(Room o) {
      return this.end - o.end;
    }
  }
  public class Lecture implements Comparable<Lecture> {
    int num;
    int start;
    int end;

    public Lecture(int num, int start, int end) {
      this.num = num;
      this.start = start;
      this.end = end;
    }
    @Override
    public int compareTo(Lecture o) {
      return this.start - o.start;
    }
  }


  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}