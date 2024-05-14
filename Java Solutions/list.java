import java.util.*;

public class list {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        
        List<Integer> L = new ArrayList<Integer>();
        for (int i = 0; i<N; i++) {
            L.add(sc.nextInt());
        }
        
        int Q = sc.nextInt();

        for (int i = 0; i<Q; i++) {
            String query = sc.next();
            if (query.equals("Insert")) {
                L.add(sc.nextInt(), sc.nextInt());                               
            }                
            else if (query.equals("Delete")) {
                L.remove(sc.nextInt());
            }
        }
        sc.close();
        for (int nums : L) {
            System.out.print(nums + " ");
        }        
    }
}
