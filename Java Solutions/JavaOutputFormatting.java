import java.util.Scanner;

public class JavaOutputFormatting {

    public static void main(String[] args) {
            Scanner sc=new Scanner(System.in);
            System.out.println("================================");
            for(int i=0;i<3;i++){
                String s1=sc.next();
                int x=sc.nextInt();
                //Complete this line
                String newX = String.valueOf(x);
                int lenX = newX.length();
                System.out.println(s1 + " ".repeat( 18-( s1.concat("0".repeat(3-lenX)).concat(newX).length() ) ) + "0".repeat(3-lenX) + newX);
            }
            System.out.println("================================");
            sc.close();
    }
}
