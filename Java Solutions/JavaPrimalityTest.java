import java.io.*;
import java.math.BigInteger;

public class JavaPrimalityTest {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        String n = bufferedReader.readLine();
        bufferedReader.close();

        BigInteger num = new BigInteger(n);

        System.out.println(num.isProbablePrime(1) ? "prime" : "not prime");
    }
}
