public class Bank {
    public static void main(String[] args) {
        // Create a SavingAccount object with name, balance, and interest rate
        SavingAccount sAccount = new SavingAccount("Anupam", 10000, 3); // Starting with Rs. 10000
        
        // Perform various operations
        sAccount.deposit(10000);  // Deposit Rs. 10,000
        try {
            sAccount.withdraw(1000000);  // Try withdrawing Rs. 1,000,000 (which will throw an exception)
        } catch (ArithmeticException e) {
            System.out.println("Error: " + e.getMessage());  // Handle exception if balance is insufficient
        }

        sAccount.addInterest();  // Adding interest
        sAccount.display();  // Display final balance
    }
}
