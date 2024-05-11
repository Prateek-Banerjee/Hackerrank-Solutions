import java.util.*;

public class JavaArrayList {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc = new Scanner (System.in);
        ArrayList<int[]> listOfLists = new ArrayList<int[]>();
        int[] arr;
        int n = sc.nextInt();
        for (int i = 0; i<n; i++) {
            int d = sc.nextInt();
            arr = new int[d];
            for (int j = 0; j<d; j++) {
                arr[j] = sc.nextInt();
            }
            listOfLists.add(arr);
        }

        int q = sc.nextInt();
        ArrayList<int[]> listOfQueries = new ArrayList<int[]>();
        int[] queries;
        for (int i = 0; i<q; i++) {
            queries = new int[2];
            for (int j = 0; j<2; j++) {
                queries[j] = sc.nextInt();
            }
            listOfQueries.add(queries);
        }
        sc.close();
        for (int i = 0; i< listOfQueries.size(); i++) {
            int[] returnedElements = listOfQueries.get(i);
            int indexOfList = returnedElements[0]-1;
            int indexOfElement = returnedElements[1]-1;
            try {
                int[] returnedList = listOfLists.get(indexOfList);
                System.out.println(returnedList[indexOfElement]);
            } catch (Exception e) {
                System.out.println("ERROR!");
            }
        }
    }
}