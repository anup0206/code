// // Question:

// // Create an abstract class Vehicle with the following:

// //     An abstract method start() that will be implemented by subclasses.
// //     A concrete method stop() that prints "The vehicle has stopped."

// // Then, create two subclasses:

// //     Car that implements start() by printing "The car starts with a key."
// //     Bike that implements start() by printing "The bike starts with a kick."




// // Abstract class Vehicle
// abstract class Vehicle {

//     // Abstract method (must be implemented by subclasses)
//     public abstract void start();

//     // Concrete method with fixed syntax
//     public void stop() {  
//         System.out.println("The vehicle has stopped.");
//     }
// }

// // Car class extending Vehicle
// class Car extends Vehicle {
//     @Override
//     public void start() {
//         System.out.println("The car starts with a key.");
//     }
// }

// // Bike class extending Vehicle
// class Bike extends Vehicle {
//     @Override
//     public void start() {
//         System.out.println("The bike starts with a kick.");
//     }
// }

// // Main class (this is where the main method is located)
// public class Main {
//     public static void main(String[] args) {
//         Car vec1 = new Car();  // Creating a Car object
//         Bike vec2 = new Bike(); // Creating a Bike object

//         vec1.start();
//         vec1.stop(); // Calls the stop() method from Vehicle

//         vec2.start();
//         vec2.stop(); // Calls the stop() method from Vehicle
//     }
// }


abstract class Shape{
    public abstract void calculateArea();
    // public void perimeter(){

    // }
}
class Circle extends Shape{
    private double radius , height;

    public Circle(double r, double h) {
        this.radius = r;
        this.height = h;
    }
    @Override
    public void calculateArea(){
        double area = 2 * Math.PI * radius * height + 2 * Math.PI * radius * radius;
        System.out.println("The area of the cylinder is: " + area);
    }


    @Override
    public void calculatePerimeter() {
        double perimeter = 2 * Math.PI * radius;
        System.out.println("The perimeter (circumference) of the base circle is: " + perimeter);
    }

}
class Rectangle extends Shape{
        private double length, breadth;

    // Constructor
    public Rectangle(double l, double b) {
        this.length = l;
        this.breadth = b;
    }


    @Override
    public void calculateArea(){
        double area = length * breadth;
        System.out.println("The area of the rectangle is: " + area);
    }

    @Override
    public void calculatePerimeter() {
        double perimeter = 2 * (length + breadth);
        System.out.println("The perimeter of the rectangle is: " + perimeter);
    }
}
public class Main{
   public static void main(String[] args){
    Circle c1 = new Circle(4,5);
    Rectangle r1= new Rectangle(5,6);

           c1.calculateArea();
        c1.calculatePerimeter();

        r1.calculateArea();
        r1.calculatePerimeter();

   }

}