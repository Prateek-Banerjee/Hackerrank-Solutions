import java.util.*;

public class JavaAnagrams {

    public static boolean anagramCheck(String a, String b) {
        char lowercaseA [] = a.toLowerCase().toCharArray();
        char lowercaseB [] = b.toLowerCase().toCharArray();

        java.util.Arrays.sort(lowercaseA);
        java.util.Arrays.sort(lowercaseB);

        return new String(lowercaseA).equals(new String(lowercaseB));
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        String b = sc.next();
        sc.close();
        
        if (anagramCheck(a, b))
            System.out.println("Anagrams");
        else
        System.out.println("Not Anagrams");
    }
}


