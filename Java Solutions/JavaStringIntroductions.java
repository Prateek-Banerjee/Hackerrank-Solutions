import java .util.*;

public class JavaStringIntroductions {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        String A=sc.next();
        String B=sc.next();
        sc.close();
        /* Enter your code here. Print output to STDOUT. */
        System.out.println(A.length()+B.length());
        System.out.println(A.compareTo(B) > 0 ? "Yes" : "No");
        System.out.println( A.replace(A.charAt(0),A.toUpperCase().charAt(0)) + " " + B.replace(B.charAt(0),B.toUpperCase().charAt(0)) );
    }    
}

