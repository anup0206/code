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

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $name = $_POST['name'];
    $gender = $_POST['gender'];
    $phone = $_POST['phone'];

    $query = "UPDATE BCA SET name='$name', gender='$gender', phone='$phone' WHERE rollno='$rollno'";

    if ($conn->query($query) === TRUE) {
        header("Location: display.php");
        exit();
    } else {
        echo "Error updating record: " . $conn->error;
    }
} else {
    $result = $conn->query("SELECT * FROM BCA WHERE rollno='$rollno'");
    $row = $result->fetch_assoc();
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Update Record</title>
</head>
<body>
    <h2>Update Record</h2>
    <form method="post">
        Name: <input type="text" name="name" value="<?= $row['name'] ?>" required><br><br>
        Gender:
        <select name="gender" required>
            <option value="Male" <?= $row['gender'] == 'Male' ? 'selected' : '' ?>>Male</option>
            <option value="Female" <?= $row['gender'] == 'Female' ? 'selected' : '' ?>>Female</option>
            <option value="Other" <?= $row['gender'] == 'Other' ? 'selected' : '' ?>>Other</option>
        </select><br><br>
        Phone: <input type="text" name="phone" value="<?= $row['phone'] ?>" required><br><br>
        <input type="submit" value="Update">
    </form>
</body>
</html>
<?php } 
header("Location: display.php");
exit();
<a href="display.php">Back to Records</a>

$conn->close(); 
?>

