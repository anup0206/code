public class Linsearch {

    public static int search(int[] arr, int targetVal) {
        for (int i = 0; i < arr.length; i++) {  // Fixed loop syntax
            if (arr[i] == targetVal) {  // Fixed if statement syntax
                return i;  // Return index if found
            }
        }
        return -1; // Return -1 if not found
    }

    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5, 9, 7}; // Example array
        int targetVal = 9; // Value to search

        int result = search(arr, targetVal); // Call the search function

        if (result != -1) {
            System.out.println("Value " + targetVal + " found at index " + result);
        } else {
            System.out.println("Value " + targetVal + " not found");
        }
    }
}
