class Solution {
    public String[] solution(int n, int[] arr1, int[] arr2) {
        String[][] bitArr = new String[n][n];
        for (int t = 0; t < 2; t++) {
          for (int i = 0; i < n; i++) {
            StringBuilder sb = new StringBuilder();
            int num;
            if (t == 0) num = arr1[i];
            else num = arr2[i];

            while (num > 0) {
              sb.append(num % 2);
              num /= 2;
            }
            int length = sb.length();
            StringBuilder zeroSb = new StringBuilder();
            for (int j = 0; j < n - length; j++) {
              zeroSb.append(0);
            }
            zeroSb.append(sb.reverse());
            bitArr[t][i] = zeroSb.toString();
          }
        }

        String[] answer = new String[n];
        for (int i = 0; i < n; i++) {
          StringBuilder sb = new StringBuilder();
          for (int j = 0; j < n; j++) {
            if (bitArr[0][i].charAt(j) == '0' && bitArr[1][i].charAt(j) == '0') {
              sb.append(" ");
            } else sb.append("#");
          }
          answer[i] = sb.toString();
        }
        return answer;
    }
}