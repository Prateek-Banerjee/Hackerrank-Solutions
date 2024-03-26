import java.util.*;
import java.math.*;

public class JavaBigInteger {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc = new Scanner(System.in);
        String num1 = sc.nextLine();
        String num2 = sc.nextLine();
        sc.close();

        System.out.println(new BigInteger(num1).add(new BigInteger(num2)));
        System.out.println(new BigInteger(num1).multiply(new BigInteger(num2)));
    }
}
