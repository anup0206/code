import java.util.Scanner;

public class Exp {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        try {
            System.out.print("Enter numerator number: ");
            double num1 = scan.nextDouble();

            System.out.print("Enter denominator number: ");
            double num2 = scan.nextDouble();

            if (num2 == 0) {
                throw new ArithmeticException("Denominator cannot be zero.");
            }

            double result = num1 / num2;
            System.out.println("The result is: " + result);
        } catch (ArithmeticException e) {
            System.out.println("Error: " + e.getMessage());
        } finally {
            scan.close();
        }
    }
}
