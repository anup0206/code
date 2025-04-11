<?php
$servername = "localhost";
$username = "root";
$password = "";
$database = "STUDENT";

$conn = new mysqli($servername, $username, $password, $database);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$rollno = $_GET['rollno'];

$query = "DELETE FROM BCA WHERE rollno='$rollno'";

if ($conn->query($query) === TRUE) {
    header("Location: display.php");
} else {
    echo "Error deleting record: " . $conn->error;
}
echo '<a href="display.php">Back to Records</a>';

$conn->close();
?>

