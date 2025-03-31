import java.util.Scanner;

public class Check {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int number = scanner.nextInt();
        
        if (number >= 0) {
            if (number > 0) {
                System.out.println("The number is positive.");
            } else {
                System.out.println("The number is zero.");
            }
        } else {
            System.out.println("The number is negative.");
        }
        
        scanner.close();
    }
}