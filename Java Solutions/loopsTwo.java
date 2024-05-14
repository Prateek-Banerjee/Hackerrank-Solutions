import java.util.*;

public class loopsTwo {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        int a=0,b=0,n=0;
        Scanner in = new Scanner(System.in);
        int t=in.nextInt();
        for(int i=0;i<t;i++){
            a = in.nextInt();
            b = in.nextInt();
            n = in.nextInt();            
            
            double sum =0;            
            for(int j=0;j<n;j++){                                
                sum += b*Math.pow(2, j);                
                //int value = (int)(a+sum);
                System.out.print((int)(a+sum)+" ");            
            }
            System.out.println();
        }
        in.close();
    }
}
