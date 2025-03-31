import java.util.Scanner;

public class DivisionExample {
    
    
    public static float divide(float num, float den) throws ArithmeticException {
        
        if (den == 0) {
            throw new ArithmeticException("Math error: Attempted to divide by zero");
        }
        
        return num / den;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
      
        System.out.print("Enter numerator: ");
        float numerator = scanner.nextFloat();
        System.out.print("Enter denominator: ");
        float denominator = scanner.nextFloat();
        
      
        try {
            float result = divide(numerator, denominator);
            System.out.println("The quotient is " + result);
        } 
        
        catch (ArithmeticException e) {
            System.out.println("Exception occurred: " + e.getMessage());
        } finally {
            scanner.close(); 
        }
    }
}