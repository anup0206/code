// Base class representing a generic Account
class Account {
    String Acc_holder;
    double balance;

    // Constructor to initialize the account with holder name and balance
    public Account(String Acc_holder, double balance) {
        this.Acc_holder = Acc_holder;
        this.balance = balance;
    }

    // Method to deposit money into the account
    public void deposit(double amount) {
        balance += amount;
        System.out.println("You have deposited Rs." + amount);
        System.out.println("The total balance of your account is Rs." + balance);
    }

    // Method to withdraw money from the account
    public void withdraw(double amount) {
        if (balance >= amount) {
            balance -= amount;
            System.out.println("You have withdrawn Rs." + amount);
        } else {
            throw new ArithmeticException("The balance is less than the amount you want to withdraw");
        }
    }

    // Method to display the account balance
    public void display() {
        System.out.println("The amount remaining in your account is Rs." + balance);
    }
}

// Subclass for SavingAccount
class SavingAccount extends Account {
    double interest;

    // Constructor to initialize SavingAccount with interest rate
    public SavingAccount(String Acc_holder, double balance, double interest) {
        super(Acc_holder, balance); // Call the superclass constructor
        this.interest = interest;
    }

    // Method to add interest to the balance
    public void addInterest() {
        double interestAmount = balance * interest / 100;
        balance += interestAmount;
        System.out.println("The interest amount added to your account is Rs." + interestAmount);
    }
}

public class Bank {
    public static void main(String[] args) {
        // Create a SavingAccount object with name, balance, and interest rate
        SavingAccount sAccount = new SavingAccount("Anupam", 10000000, 3);
        
        // Perform various operations
        sAccount.deposit(10000);
        sAccount.withdraw(1000000);
        sAccount.addInterest();  // Adding interest
        sAccount.display();  // Display final balance
    }
}
