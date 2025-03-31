class Queseven {
  
    public Queseven() {
        System.out.println("This is a parent class");
    }
}

class Subclass extends Queseven {
    
    public Subclass() {
        System.out.println("This is a child class");
    }
}

public class Maine{
    public static void main(String[] args) {
        
        Queseven parentObj = new Queseven(); 
        
       
        Subclass childObj = new Subclass(); 
        
      
        Queseven parentRefChild = new Subclass(); 

    }
}