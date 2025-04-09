import javax.swing.*;
import java.awt.event.*;
import java.io.*;

public class FullSwingForm {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Registration Form");
        frame.setSize(600, 600); // Increased height to accommodate new fields
        frame.setLayout(null);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        // --- Name
        JLabel nameLabel = new JLabel("Name:");
        nameLabel.setBounds(20, 20, 100, 25);
        JTextField nameField = new JTextField();
        nameField.setBounds(140, 20, 200, 25);
        frame.add(nameLabel);
        frame.add(nameField);

        // --- Email
        JLabel emailLabel = new JLabel("Email:");
        emailLabel.setBounds(20, 60, 100, 25);
        JTextField emailField = new JTextField();
        emailField.setBounds(140, 60, 200, 25);
        frame.add(emailLabel);
        frame.add(emailField);

        // --- Phone
        JLabel phoneLabel = new JLabel("Phone:");
        phoneLabel.setBounds(20, 100, 100, 25);
        JTextField phoneField = new JTextField();
        phoneField.setBounds(140, 100, 200, 25);
        frame.add(phoneLabel);
        frame.add(phoneField);

        // --- Gender
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

        // --- Country
        JLabel countryLabel = new JLabel("Country:");
        countryLabel.setBounds(20, 180, 100, 25);
        String[] countries = {"India", "USA", "UK", "Canada", "Australia", "Nepal"};
        JComboBox<String> countryBox = new JComboBox<>(countries);
        countryBox.setBounds(140, 180, 200, 25);
        frame.add(countryLabel);
        frame.add(countryBox);

        // --- Shift (New Field)
        JLabel shiftLabel = new JLabel("Shift:");
        shiftLabel.setBounds(20, 220, 100, 25);
        String[] shifts = {"Morning", "Afternoon", "Evening"};
        JComboBox<String> shiftBox = new JComboBox<>(shifts);
        shiftBox.setBounds(140, 220, 200, 25);
        frame.add(shiftLabel);
        frame.add(shiftBox);

        // --- Message
        JLabel messageLabel = new JLabel("Message:");
        messageLabel.setBounds(20, 260, 100, 25);
        JTextArea messageArea = new JTextArea();
        messageArea.setBounds(140, 260, 200, 80);
        frame.add(messageLabel);
        frame.add(messageArea);

        // --- Remarks (New Field)
        JLabel remarksLabel = new JLabel("Remarks:");
        remarksLabel.setBounds(20, 360, 100, 25);
        JTextArea remarksArea = new JTextArea();
        remarksArea.setBounds(140, 360, 200, 80);
        frame.add(remarksLabel);
        frame.add(remarksArea);

        // --- Submit Button
        JButton submitButton = new JButton("Submit");
        submitButton.setBounds(80, 460, 100, 30);
        frame.add(submitButton);

        // --- Reset Button
        JButton resetButton = new JButton("Reset");
        resetButton.setBounds(200, 460, 100, 30);
        frame.add(resetButton);

        // --- Action for Submit
        submitButton.addActionListener(e -> {
            String name = nameField.getText().trim();
            String email = emailField.getText().trim();
            String phone = phoneField.getText().trim();
            String gender = maleBtn.isSelected() ? "Male" :
                            femaleBtn.isSelected() ? "Female" :
                            otherBtn.isSelected() ? "Other" : "";
            String country = (String) countryBox.getSelectedItem();
            String shift = (String) shiftBox.getSelectedItem();
            String message = messageArea.getText().trim();
            String remarks = remarksArea.getText().trim();

            // --- VALIDATION
            if (name.isEmpty() || email.isEmpty() || phone.isEmpty()) {
                JOptionPane.showMessageDialog(frame, "Name, Email, and Phone cannot be empty.", "Validation Error", JOptionPane.ERROR_MESSAGE);
                return;
            }

            // --- SAVE TO FILE
            try {
                FileWriter writer = new FileWriter("form_data.txt", true); // true = append mode
                writer.write("Name: " + name + "\n");
                writer.write("Email: " + email + "\n");
                writer.write("Phone: " + phone + "\n");
                writer.write("Gender: " + gender + "\n");
                writer.write("Country: " + country + "\n");
                writer.write("Shift: " + shift + "\n");
                writer.write("Message: " + message + "\n");
                writer.write("Remarks: " + remarks + "\n");
                writer.write("---------------\n");
                writer.close();
                JOptionPane.showMessageDialog(frame, "Form submitted and saved to file!");
            } catch (IOException ex) {
                JOptionPane.showMessageDialog(frame, "Error saving to file!", "File Error", JOptionPane.ERROR_MESSAGE);
            }
        });

        // --- Action for Reset
        resetButton.addActionListener(e -> {
            nameField.setText("");
            emailField.setText("");
            phoneField.setText("");
            genderGroup.clearSelection();
            countryBox.setSelectedIndex(0);
            shiftBox.setSelectedIndex(0);
            messageArea.setText("");
            remarksArea.setText("");
        });

        frame.setVisible(true);
    }
}
