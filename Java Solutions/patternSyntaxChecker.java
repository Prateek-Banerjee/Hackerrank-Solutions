import java.util.*;
import java.util.regex.*;

public class patternSyntaxChecker
{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int testCases = Integer.parseInt(sc.nextLine());
        while(testCases>0){
            String pattern = sc.nextLine();
              //Write your code
            try {
                Pattern.compile(pattern);
                System.out.println("Valid");
            } catch (Exception e) {
                System.out.println("Invalid");
            }
            testCases--;
        }
        sc.close();
    }
}