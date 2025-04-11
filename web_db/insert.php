<?php
// Database connection
$servername = "localhost";
$username = "root";     
$password = "";         
$database = "STUDENT";


$conn = new mysqli($servername, $username, $password, $database);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Get form data
$rollno = $_POST['rollno'];
$name = $_POST['name'];
$gender = $_POST['gender'];
$phone = $_POST['phone'];

$inser = "INSERT INTO BCA (rollno ,name,gender,phone) VALUES ('$rollno','$name','$gender','$phone')";

$run = mysqli_query($conn , $inser);

// Execute the query
if ($run == true) {
    echo "Record inserted successfully!";
} else {
    echo "Error: " . $stmt->error;
}


// Close connection

$conn->close();
?>

