class A{
 void methodA(){
    System.out.println("Output from A");

 }

}
class B extends A{
    void methodB
    ()
        {
         System.out.println("Output from B");


    }
}

class C extends B{
    void methodC(){
         System.out.println("Output from c");


    }
}
public class Multi{
    public static void main(String[] args){
        C obj = new C();
        obj.methodA();
        obj.methodB();
        obj.methodC();

    }
}

