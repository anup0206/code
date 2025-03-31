import java.util.Random;  // Import Random class

public class RandomNumberGenerator {
    public static void main(String[] args) {
        Random rand = new Random();  // Create an instance of Random

        int randomNumber = rand.nextInt(100);  // Generate a random number between 0-99
        System.out.println("Random Number: " + randomNumber);
    }
}
