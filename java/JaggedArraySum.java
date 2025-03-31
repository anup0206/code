public class JaggedArraySum {
    public static void main(String[] args) {
        // Initializing a jagged array with different row sizes
        int[][] jaggedArray = {
            {1, 2, 3},
            {4, 5},
            {6, 7, 8, 9}
        };
        
        // Loop through each row of the jagged array
        for (int i = 0; i < jaggedArray.length; i++) {
            int sum = 0;
            System.out.print("Row " + (i + 1) + " elements: ");
            
            // Loop through each element of the current row
            for (int j = 0; j < jaggedArray[i].length; j++) {
                System.out.print(jaggedArray[i][j] + " ");
                sum += jaggedArray[i][j];
            }
            
            // Displaying the sum of the row
            System.out.println("| Row Sum: " + sum);
        }
    }
}
