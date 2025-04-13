import javax.swing.*;
import java.awt.*;

public class Develop {
    public static void main(String[] args) {
        JFrame frame = new JFrame("INFO FORM");
        frame.setSize(600, 600);
        frame.setLayout(null);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        // NAME
        JLabel nameLabel = new JLabel("Name:");
        nameLabel.setBounds(20, 20, 100, 25);
        JTextField nameField = new JTextField();
        nameField.setBounds(140, 20, 200, 25);
        frame.add(nameLabel);
        frame.add(nameField);

        // CLASS
        JLabel classLabel = new JLabel("Class:");
        classLabel.setBounds(20, 60, 100, 25);
        JTextField classField = new JTextField();
        classField.setBounds(140, 60, 200, 25);
        frame.add(classLabel);
        frame.add(classField);

        // CONTACT NUMBER
        JLabel contactLabel = new JLabel("Contact No.:");
        contactLabel.setBounds(20, 100, 100, 25);
        JTextField contactField = new JTextField();
        contactField.setBounds(140, 100, 200, 25);
        frame.add(contactLabel);
        frame.add(contactField);

        // GENDER
        JLabel genderLabel = new JLabel("Gender:");
        genderLabel.setBounds(20, 140, 100, 25);
        JRadioButton maleBtn = new JRadioButton("Male");
        maleBtn.setBounds(140, 140, 60, 25);
        JRadioButton femaleBtn = new JRadioButton("Female");
        femaleBtn.setBounds(200, 140, 70, 25);
        JRadioButton otherBtn = new JRadioButton("Other");
        otherBtn.setBounds(270, 140, 70, 25);
        ButtonGroup genderGroup = new ButtonGroup();
        genderGroup.add(maleBtn);
        genderGroup.add(femaleBtn);
        genderGroup.add(otherBtn);
        frame.add(genderLabel);
        frame.add(maleBtn);
        frame.add(femaleBtn);
        frame.add(otherBtn);

        // COUNTRY
        JLabel countryLabel = new JLabel("Country:");
        countryLabel.setBounds(20, 180, 100, 25);
        String[] countries = {"Nepal", "Japan", "India", "UK", "USA", "Australia", "Korea"};
        JComboBox<String> countryBox = new JComboBox<>(countries);
        countryBox.setBounds(140, 180, 200, 25);
        frame.add(countryLabel);
        frame.add(countryBox);

        // MESSAGE
        JLabel messageLabel = new JLabel("Message:");
        messageLabel.setBounds(20, 220, 100, 25);
        JTextArea messageField = new JTextArea();
        messageField.setBounds(140, 220, 200, 80);
        frame.add(messageLabel);
        frame.add(messageField);

        // SUBMIT BUTTON
        JButton submitButton = new JButton("Submit");
        submitButton.setBounds(80, 320, 100, 30);
        frame.add(submitButton);

        frame.setVisible(true); 
    }
}
