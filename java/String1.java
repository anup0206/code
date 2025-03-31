
import java.util.Scanner;
public class String1 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.println("Enter your  first name");
        String fname = scan.nextLine();

        System.out.println("Enter your last name");
        String lname = scan.nextLine();

        String name = fname +" " + lname ;
        
        System.out.println("Ohayo "+ name);

        System.out.println("The length of your name is " + name.length());



        
        

    }
}