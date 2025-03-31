public class MethodOverloading {

    // Method to add two integers
    public static int add(int a, int b) {
        return a + b;
    }

    // Method to add two double values
    public static double add(double a, double b) {
        return a + b;
    }

    // Method to add three integers
    public static int add(int a, int b, int c) {
        return a + b + c;
    }

    public static void main(String[] args) {
        int intResult = add(5, 10); // Calls the first add method
        double doubleResult = add(5.5, 10.5); // Calls the second add method
        int threeIntResult = add(1, 2, 3); // Calls the third add method

        System.out.println("Sum of two integers: " + intResult);
        System.out.println("Sum of two doubles: " + doubleResult);
        System.out.println("Sum of three integers: " + threeIntResult);
    }
}