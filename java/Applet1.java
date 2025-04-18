
import java.applet.Applet;
import java.awt.Graphics;

public class Applet1 extends Applet {
    @Override
    public void paint(Graphics g) {
        g.drawString("Hello, World!" , 20,20);
    }
}