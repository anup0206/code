import javax.swing.*;
import java.awt.event.*;

public class Calculate {

    public static void main(String[] args) {
        JFrame frame = new JFrame("Calculator");
        frame.setSize(400, 300); 
        frame.setLayout(null);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        JLabel NUM1 = new JLabel("num1");
        NUM1.setBounds(20, 20, 100, 25);
        JTextField NUM1field = new JTextField();
        NUM1field.setBounds(140, 20, 200, 25);
        frame.add(NUM1);
        frame.add(NUM1field); 

        JLabel NUM2 = new JLabel("num2");
        NUM2.setBounds(20, 60, 100, 25);
        JTextField NUM2field = new JTextField();
        NUM2field.setBounds(140, 60, 200, 25);
        frame.add(NUM2);
        frame.add(NUM2field);

        JLabel resultLabel = new JLabel("Result: ");
        resultLabel.setBounds(20, 140, 320, 25);
        frame.add(resultLabel);

        JButton submitButton = new JButton("CALCULATE");
        submitButton.setBounds(140, 100, 120, 30);
        frame.add(submitButton);

        submitButton.addActionListener(e -> {
            try {
                int num1 = Integer.parseInt(NUM1field.getText());
                int num2 = Integer.parseInt(NUM2field.getText());
                int result = num1 + num2;

                resultLabel.setText("Result: " + result);
            } catch (NumberFormatException ex) {
                resultLabel.setText("Please enter valid numbers.");
            }
        });

        frame.setVisible(true);
    }
}
