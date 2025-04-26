<?php
header('Content-Type: application/json');

// Database configuration
$host = 'localhost';
$dbname = 'feedback_db';
$username = 'your_username'; // Replace with your MySQL username
$password = 'your_password'; // Replace with your MySQL password

try {
    // Create PDO connection
    $pdo = new PDO("mysql:host=$host;dbname=$dbname", $username, $password);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    // Get form data
    $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_SANITIZE_EMAIL);
    $phone = filter_input(INPUT_POST, 'phone', FILTER_SANITIZE_STRING);
    $feedback_type = filter_input(INPUT_POST, 'feedback_type', FILTER_SANITIZE_STRING);
    $satisfaction = filter_input(INPUT_POST, 'satisfaction', FILTER_SANITIZE_STRING);
    $comments = filter_input(INPUT_POST, 'comments', FILTER_SANITIZE_STRING);

    // Validate required fields
    if (empty($name) || empty($email) || empty($feedback_type) || empty($satisfaction)) {
        echo json_encode(['success' => false, 'message' => 'Please fill all required fields.']);
        exit;
    }

    // Prepare and execute SQL query
    $stmt = $pdo->prepare("
        INSERT INTO submissions (name, email, phone, feedback_type, satisfaction, comments, created_at)
        VALUES (:name, :email, :phone, :feedback_type, :satisfaction, :comments, NOW())
    ");
    $stmt->execute([
        ':name' => $name,
        ':email' => $email,
        ':phone' => $phone,
        ':feedback_type' => $feedback_type,
        ':satisfaction' => $satisfaction,
        ':comments' => $comments
    ]);

    echo json_encode(['success' => true, 'message' => 'Thank you for your feedback!']);
} catch (PDOException $e) {
    echo json_encode(['success' => false, 'message' => 'Database error: ' . $e->getMessage()]);
} catch (Exception $e) {
    echo json_encode(['success' => false, 'message' => 'An error occurred: ' . $e->getMessage()]);
}
?>