<?php
error_reporting(E_ALL);
ini_set('display_errors', 1);

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
echo "Connected successfully<br>";

$query = "SELECT * FROM BCA";
$data = mysqli_query($conn, $query);

if (!$data) {
    die("Query failed: " . mysqli_error($conn));
}

$total = mysqli_num_rows($data);

if ($total != 0) {
    echo "<table border='1' cellspacing='0' cellpadding='10'>
            <tr>
                <th>rollno</th>
                <th>name</th>
                <th>gender</th>
                <th>phone</th>
                <th>Update</th>
                <th>Delete</th>
            </tr>";

    while ($result = mysqli_fetch_assoc($data)) {
        echo "<tr>
                <td>{$result['rollno']}</td>
                <td>" . htmlspecialchars($result['name']) . "</td>
                <td>{$result['gender']}</td>
                <td>{$result['phone']}</td>
                <td><a href='update.php?rollno={$result['rollno']}'>Update</a></td>
                <td><a href='delete.php?rollno={$result['rollno']}' onclick='return confirm(\"Are you sure?\");'>Delete</a></td>
              </tr>";
    }

    echo "</table>";
} else {
    echo "No records found.";
}

$conn->close();
?>

<a href="form.php" style="display:block; text-align:center; margin-top:10px;">Back to Form</a>

