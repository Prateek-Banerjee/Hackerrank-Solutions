import java.util.*;

public class JavaStaticInitializerBlock {    
    private static int b,h;
    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc = new Scanner(System.in);
        b = sc.nextInt();
        h = sc.nextInt();
        sc.close();
        try{
            if (((b > 0) && (b <= 100)) && ((h > 0) && (h <= 100)))
                System.out.println(b*h);
            else
                throw new Exception("Breadth and height must be positive");
        }
        catch(Exception e)
        {
            System.out.println(e);
        }   
    }
}