import java.io.*;
import java.util.*;

import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;

import com.google.gson.Gson;

public class Main {


  public String solution2_2() throws Exception {

    Reader reader = new FileReader("C:/Users/gun kim/Downloads/data.json");
    // reader를 Object로 parse
    JSONParser parser = new JSONParser();
    Object obj = parser.parse(reader);

    // obj를 JsonArray로 cast
    JSONArray jsonArr = (JSONArray)obj;

    ArrayList<Person> people = new ArrayList<>();
    // jsonArr에서 하나씩 JSONObject로 cast해서 사용
    if (jsonArr.size() > 0) {
      for (int i = 0; i < jsonArr.size(); i++) {

        JSONObject jsonObj = (JSONObject)jsonArr.get(i);

        String name = (String)jsonObj.get("name");
        Long scoreLong = (Long)jsonObj.get("score");
        int score = scoreLong.intValue();

        people.add(new Person(name, score));
      }
    }

    Collections.sort(people);

    Gson gson = new Gson();
    String jsonStr = gson.toJson(people.get(0));

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

  public class Person implements Comparable<Person> {
    private String name;
    private int score;

    public Person(String name, int score) {
      this.name = name;
      this.score = score;
    }

    @Override
    public int compareTo(Person o) {
      return o.name.compareTo(this.name);
    }
  }


  public static void main(String[] args) throws Exception {

    new Main().solution2_2();
  }

}