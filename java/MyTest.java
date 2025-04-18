import java.io.*;

class StudentInfo implements Serializable {
    String name;
    int rid;
    static String contact;
    StudentInfo(String n,int r ,String c ){
        this.name = n;
        this.rid = r;
        this.contact = c;

    }
}
public class MyTest{
    public static void main (String[] args){
        try{
            StudentInfo si = new StudentInfo("anupam", 0206,"302");
            FileOutputStream fos = new FileOutputStream("student.ser");
            ObjectOutputStream oos = new ObjectOutputStream(fos);
            oos.writeObject(si);
            oos.close();
            fos.close();
        }
        catch(Exception e){
            e.printStackTrace();

        }
    }
}