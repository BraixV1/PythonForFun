
import java.math.*;
import java.util.Arrays;
import java.util.Random;

public class Code {

    public static void main(String[] args) {

        int[] numbers = {1, 3, -2, 9};
        System.out.println(average(numbers));
        System.out.println(minimumElement(numbers));
        System.out.println(sum(numbers)); // 11
        System.out.println(asString(numbers));
    }

    public static int sum(int[] numbers) {
        int x = 0;
        for (int i = 0; i < numbers.length; i++) {
            x += numbers[i];
        }
        return x;
    }

    public static double average(int[] numbers) {
        Double x = 0.0;
        for (int i = 0; i < numbers.length; i++) {
            x += numbers[i];
        }
        double y = Double.valueOf(x / numbers.length);
        return y;
    }

    public static Integer minimumElement(int[] integers) {
        if(integers.length == 0) {
            return null;
        }
        Integer first = integers[0];
        for (int i = 1; i < integers.length; i++) {
            if(first > integers[i]) {
                first = integers[i];
            }
        }
        return first;
    }

    public static String asString(int[] elements) {
        String result = "";
        for (int i = 0; i < elements.length - 1; i++) {
            result += String.valueOf(elements[i]);
            result += ", ";
        }
        result += String.valueOf(elements[elements.length -1]);
        return result;
    }

    public static Character mode(String input) {
        return null;
    }

    public static String squareDigits(String s) {
        return "";
    }

    public static int isolatedSquareCount() {
        boolean[][] matrix = getSampleMatrix();

        printMatrix(matrix);

        int isolatedCount = 0;

        // count isolates squares here

        return isolatedCount;
    }

    private static void printMatrix(boolean[][] matrix) {
        for (boolean[] row : matrix) {
            System.out.println(Arrays.toString(row));
        }
    }

    private static boolean[][] getSampleMatrix() {
        boolean[][] matrix = new boolean[10][10];

        Random r = new Random(5);
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[0].length; j++) {
                matrix[i][j] = r.nextInt(5) < 2;
            }
        }

        return matrix;
    }
}
