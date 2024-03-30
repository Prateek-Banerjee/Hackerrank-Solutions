import java.util.*;

public class JavaEndOfFile {
    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc = new Scanner(System.in);
        int lineNumber = 1;
        
        while (sc.hasNext()) {
            System.out.println(lineNumber + " " + sc.nextLine());
            lineNumber += 1;
        }
        sc.close();
    }
}