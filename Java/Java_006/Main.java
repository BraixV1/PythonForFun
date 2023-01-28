package Java.Java_006;
import java.util.Scanner;
// Learning java logical operators

public class Main {
    public static void main(String[] args) {
        // Logical operators:
        // && = AND
        // || = OR
        // ! = NOT
    Scanner scanner = new Scanner(System.in);
    int temp = scanner.nextInt();
    scanner.nextLine();
    
    if(temp>35) {
        System.out.println("It is hot outside!");
    }
    else if(temp>=20 && temp<=35) {
        System.out.println("It is warm outside");
    }
    else {
        System.out.println("It is cold outside");
    }
    scanner.close();
    }

}
