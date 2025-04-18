import java.lang.Math;
import java.util.Scanner;

public class LangMathUserInput {
    public static void main(String[] args) {
        // Create Scanner object for user input
        Scanner scanner = new Scanner(System.in);

        // Get input for absolute value calculation
        System.out.print("Enter an integer for absolute value calculation: ");
        int value1 = scanner.nextInt();

        // Get input for trigonometric functions
        System.out.print("Enter a double value (between -1 and 1) for trigonometric calculations: ");
        double value2 = scanner.nextDouble();

        // Get input for cube root and square root
        System.out.print("Enter a number for cube root and square root calculations: ");
        double value3 = scanner.nextDouble();

        // Get input for ceil and floor
        System.out.print("Enter a decimal number for ceil and floor calculations: ");
        double value4 = scanner.nextDouble();

        // Perform calculations and display results
        System.out.println("\nResults:");
        System.out.println("Absolute value = " + Math.abs(value1));
        
        System.out.println("ACos value = " + Math.acos(value2));
        System.out.println("ATan value = " + Math.atan(value2));
        System.out.println("ASin value = " + Math.asin(value2));
        
        System.out.println("Cube root = " + Math.cbrt(value3));
        System.out.println("Square root = " + Math.sqrt(value3));
        
        System.out.println("Ceil value = " + Math.ceil(value4));
        System.out.println("Floor value = " + Math.floor(value4));

        // Close scanner
        scanner.close();
    }
}