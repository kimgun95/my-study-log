import java.io.*;
import java.util.*;

import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;

import com.google.gson.Gson;

public class Main {


  public String solution2_1() throws Exception {

    Reader reader = new FileReader("C:/Users/gun kim/Downloads/data.json");
    // reader를 Object로 parse
    JSONParser parser = new JSONParser();
    Object obj = parser.parse(reader);

    // obj를 JsonArray로 cast
    JSONArray jsonArr = (JSONArray)obj;

    int sum = 0;
    int size = 0;
    int minScore = Integer.MAX_VALUE;
    int maxScore = Integer.MIN_VALUE;
    Map<Integer, ArrayList<Person>> map = new HashMap<>();
    // jsonArr에서 하나씩 JSONObject로 cast해서 사용
    if (jsonArr.size() > 0) {
      for (int i = 0; i < jsonArr.size(); i++) {

        JSONObject jsonObj = (JSONObject)jsonArr.get(i);

        String name = (String)jsonObj.get("name");
        Long scoreLong = (Long)jsonObj.get("score");
        int score = scoreLong.intValue();

        sum += score;
        size++;
        minScore = Math.min(minScore, score);
        maxScore = Math.max(maxScore, score);

        ArrayList<Person> arrayList = map.getOrDefault(score, new ArrayList<>());
        arrayList.add(new Person(name, score));
        map.put(score, arrayList);
      }
    }
    int avg = sum / size;
    PrintData printData = new PrintData(avg, map.get(minScore), map.get(maxScore));
    Gson gson = new Gson();
    String jsonStr = gson.toJson(printData);

    System.out.println(jsonStr);
    return "";
  }

  public class PrintData {
    private int avg;
    private ArrayList<Person> min;
    private ArrayList<Person> max;

    public PrintData(int avg, ArrayList<Person> minScoreList, ArrayList<Person> maxScoreList) {
      this.avg = avg;
      this.min = minScoreList;
      this.max = maxScoreList;
    }
  }

  public class Person {
    private String name;
    private int score;

    public Person(String name, int score) {
      this.name = name;
      this.score = score;
    }
  }


  public static void main(String[] args) throws Exception {

    new Main().solution2_1();
  }

}