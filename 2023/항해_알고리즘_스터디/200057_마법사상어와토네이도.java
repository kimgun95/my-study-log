package org.example;

import java.io.*;
import java.util.*;

public class Main {

  static int[][] dir = {{0, -1}, {1, 0}, {0, 1}, {-1, 0}}; // 서,남,동,북 방향
  static boolean[][] visit; // 모래 폭풍이 지나간 자리는 방문 처리
  static int[][] sand; // 좌표마다 모래가 쌓인 값 저장
  static int n;
  static int answer; // 밖으로 날아간 모래의 총량

  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    n = Integer.parseInt(br.readLine());
    sand = new int[n + 1][n + 1];
    StringTokenizer st;
    for (int i = 1; i <= n; i++) {
      st = new StringTokenizer(br.readLine());
      for (int j = 1; j <= n; j++) {
        sand[i][j] = Integer.parseInt(st.nextToken());
      }
    }

    visit = new boolean[n + 1][n + 1];
    int coordinate = n / 2 + 1; // 시작 좌표
    visit[coordinate][coordinate] = true;
    answer = 0;
    // 모래 폭풍 시작
    wind(coordinate, coordinate, 0);

    System.out.println(answer);
  }

  private void wind(int y, int x, int direction) {
    // 모래의 분산을 계산
    dispersion(y, x, direction);
    // 다음으로 이동할 좌표 계산
    int sy = y + dir[direction][0];
    int sx = x + dir[direction][1];
    if (sy == 1 && sx == 1) {
      return;
    }

    // 왼쪽 방향 방문 여부 : 방문했다면 직진, 안했다면 왼쪽으로 이동
    int ny = sy + dir[(direction + 1) % 4][0];
    int nx = sx + dir[(direction + 1) % 4][1];
    if (visit[ny][nx]) wind(sy, sx, direction);
    else wind(sy, sx, (direction + 1) % 4);
  }

  // 모래 분산
  private void dispersion(int y, int x, int direction) {
    int ny = y + dir[direction][0];
    int nx = x + dir[direction][1];
    int initSand = sand[ny][nx]; // 최초 모래양
    int total = sand[ny][nx]; // 분산시키고 남는 모래양 저장
    // 왼쪽 1%
    total -= calculate(initSand, y, x, (direction + 1) % 4, 1, 1);
    // 오른쪽 1%
    total -= calculate(initSand, y, x, (direction - 1 + 4) % 4, 1, 1);
    // 왼쪽 7%
    total -= calculate(initSand, y + dir[direction][0], x + dir[direction][1], (direction + 1) % 4, 7, 1);
    // 오른쪽 7%
    total -= calculate(initSand, y + dir[direction][0], x + dir[direction][1], (direction - 1 + 4) % 4, 7, 1);
    // 왼쪽 2%
    total -= calculate(initSand, y + dir[direction][0], x + dir[direction][1], (direction + 1) % 4, 2, 2);
    // 오른쪽 2%
    total -= calculate(initSand, y + dir[direction][0], x + dir[direction][1], (direction - 1 + 4) % 4, 2, 2);
    // 왼쪽 10%
    total -= calculate(initSand, y + dir[direction][0] * 2, x + dir[direction][1] * 2, (direction + 1) % 4, 10, 1);
    // 오른쪽 10%
    total -= calculate(initSand, y + dir[direction][0] * 2, x + dir[direction][1] * 2, (direction - 1 + 4) % 4, 10, 1);
    // 5%
    total -= calculate(initSand, y + dir[direction][0] * 2, x + dir[direction][1] * 2, direction, 5, 1);
    // 알파
    int ay = y + dir[direction][0] * 2;
    int ax = x + dir[direction][1] * 2;
    if (ay >= 1 && ay <= n && ax >= 1 && ax <= n) {
      sand[ay][ax] += total;
    } else {
      answer += total;
    }

    visit[ny][nx] = true;
  }

  // 분산량 계산
  private int calculate(int initAmount, int y, int x, int idx, int percent, int move) {
    int ny = y + dir[idx][0] * move;
    int nx = x + dir[idx][1] * move;
    int amount = initAmount * percent / 100;

    if (ny >= 1 && ny <= n && nx >= 1 && nx <= n) {
      sand[ny][nx] += amount;
    } else {
      answer += amount;
    }
    return amount;
  }


  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}