import java.io.*;
import java.util.*;

public class twoDArray {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        List<List<Integer>> arr = new ArrayList<>();

        for (int i = 0; i < 6; i++) {
            String[] arrRowTempItems = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

            List<Integer> arrRowItems = new ArrayList<>();

            for (int j = 0; j < 6; j++) {
                int arrItem = Integer.parseInt(arrRowTempItems[j]);
                arrRowItems.add(arrItem);
            }

            arr.add(arrRowItems);
        }
        bufferedReader.close();
        int maxHourglassSum = Integer.MIN_VALUE;;
        for (int row = 0; row <= 3; row++) {
            for (int column = 0; column <= 3; column++) {
                int tempSum = ((arr.get(row)).get(column)) + ((arr.get(row)).get(column+1)) + ((arr.get(row)).get(column+2)) + ((arr.get(row+1)).get(column+1)) + ((arr.get(row+2)).get(column)) + ((arr.get(row+2)).get(column+1)) + ((arr.get(row+2)).get(column+2));
                if (tempSum > maxHourglassSum) {
                    maxHourglassSum = tempSum;
                }
            }
        }
        System.out.println(maxHourglassSum);
    }
}
