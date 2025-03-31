public class OddInt {
    // Declare and initialize an array with 'f' suffix for float values
    float[] arr = {1f, 3f, 4f, 2f, 5f, 6f, 24f, 56f, 76f, 77f, 97f, 92.6f, 99.3f};
    float sum = 0;

    // Constructor to calculate the sum of odd integers
    public OddInt() {
        for (float num : arr) {
            if (num % 2 != 0) { // Check for odd numbers
                sum += num;
            }
        }
    }

    // Main method to execute the program
    public static void main(String[] args) {
        OddInt obj = new OddInt();
        System.out.println("The sum of odd integers in the array is: " + obj.sum);
    }
}
