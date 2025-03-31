import java.util.Scanner;
import java.util.ArrayList;

public class Const {
    String name;
    String studentClass; // Renamed to avoid keyword conflict
    int age;
    String college; // Fixed spelling from "collage" to "college"
    int rollno;

    // Constructor
    public Const(String name, String studentClass, int age, String college, int rollno) {
        this.name = name;
        this.studentClass = studentClass;
        this.age = age;
        this.college = college;
        this.rollno = rollno;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter the number of students you want to enter: ");
        int num = sc.nextInt();

        // List to store student objects
        ArrayList<Const> students = new ArrayList<>();

        for (int i = 0; i < num; i++) {
            sc.nextLine(); // Consume newline

            System.out.println("\nEnter the data of student " + (i + 1) + ":");

            System.out.print("Enter the name: ");
            String name = sc.nextLine();

            System.out.print("Enter the class: ");
            String studentClass = sc.nextLine();

            System.out.print("Enter the age: ");
            int age = sc.nextInt();
            sc.nextLine(); // Consume newline

            System.out.print("Enter the college name: ");
            String college = sc.nextLine();

            System.out.print("Enter the roll number: ");
            int rollno = sc.nextInt();

            // Creating and storing student objects
            students.add(new Const(name, studentClass, age, college, rollno));
        }

        // Displaying stored student data
        System.out.println("\nStored Student Data:");
        for (int i = 0; i < students.size(); i++) {
            Const obj = students.get(i);
            System.out.println("\nStudent " + (i + 1) + " details:");
            System.out.println("Name: " + obj.name);
            System.out.println("Class: " + obj.studentClass);
            System.out.println("Age: " + obj.age);
            System.out.println("College: " + obj.college);
            System.out.println("Roll Number: " + obj.rollno);
        }

        sc.close();
    }
}
