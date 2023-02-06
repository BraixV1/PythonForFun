package Java.java_007;
// Learning java 007 actual lesson from java course in university.


public class Main {
    public static void main(String[] args) {
        System.out.println(pow(5, 2));
        System.out.println(asDecimal("00011011"));
        System.out.println(asString(255));
    }

    public static String asString(int input) {
        String result = "";
        String done = "";

        while(input >= 1) {
            if(input == 0){
                break;
            }
            int remainder = input % 2;
            if(remainder == 0) {
                input = input / 2;
                result += "0";
            } else {
                input = input / 2;
                result += "1";
            }
      
        }
        
        for (int i = result.length(); i > 0; i--) {
            done += result.charAt(i-1); 
        } 

        return done;
        
    }

    public static int asDecimal(String input) {
        int result = 0;
        int repeater = 0;
        for (int i = input.length(); i > 0; i--) {
            char number = input.charAt(i-1);
            int x = number - '0';
            result += x * pow(2, repeater);
            repeater ++;

        }
        return result;

    }

    private static int pow(int arg, int power) {
        // Java has Math.pow() but this time write your own implementation.
        int result = 1;
        if(arg == 0) {
            return result;
        }
        for (int i = 0; i < power ; i++) {
            result *= arg;

        }

        return result;
    }
}
