import java.util.*;

public class subArray {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];

        for(int i = 0; i<n;i++ ) {
            arr[i] = sc.nextInt();
        }
        sc.close();
        int negativeSumCount = 0;
        int sum = 0;
        for (int i = 0; i < arr.length; i++) {
            sum = arr[i];
            if (sum < 0)
                negativeSumCount++;
            for (int j = i+1; j<arr.length;j++) {
                sum+=arr[j];
                if (sum < 0)
                    negativeSumCount++;
            }
        }

        System.out.println(negativeSumCount);
    }
}