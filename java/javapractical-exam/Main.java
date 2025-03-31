class Student {
    private String name;
    private int age;

    // Constructor to initialize name and age
    public Student(String name, int age) {
        this.name = name;
        this.age = age;
    }

    // Method to display student details
    public void displayDetails() {
        System.out.println("Student Name: " + name);
        System.out.println("Student Age: " + age);
    }
}

public class Main {
    public static void main(String[] args) {
        // Creating a Student object
        Student student1 = new Student("Alice", 20);
        
        // Displaying the details of the student
        student1.displayDetails();
    }
}