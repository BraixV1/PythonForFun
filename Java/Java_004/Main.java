// Java learning 004 Random module
package Java.Java_004;
import java.util.Random;

public class Main {
    public static void main(String[] args) {
        

        Random random = new Random();

        int x = random.nextInt(-10, 10);
        //double y = random.nextDouble();
        boolean z = random.nextBoolean();

        System.out.println(x);
        System.out.println(z);
    }
}
