import java.util.*;
public class stringReverse {
    public static void main(String[] args) {
        
        Scanner sc=new Scanner(System.in);
        String A=sc.next();
        sc.close();
        /* Enter your code here. Print output to STDOUT. */
        StringBuilder sb = new StringBuilder(A);
        if (A.equals(sb.reverse().toString()))
            System.out.println("Yes");
        else
            System.out.println("No");
    }
}
