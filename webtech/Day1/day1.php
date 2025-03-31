<?php 
session_start(); 

$validname = "admin";  
$hashedPass = password_hash("password", PASSWORD_DEFAULT); // Store this securely in DB

$error = ""; // Initialize error variable

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = $_POST['username'] ?? '';
    $password = $_POST['password'] ?? '';

    if ($username == $validname && password_verify($password, $hashedPass)) {
        $_SESSION['loggedin'] = true;
        echo "Logged in";
    } else {
        $error = "Error: Login failed. Wrong username or password.";
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login Page</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f9;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }

        .login-container {
            background-color: #fff;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            width: 300px;
        }

        h2 {
            text-align: center;
            margin-bottom: 20px;
        }

        .input-field {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 5px;
        }

        .btn {
            width: 100%;
            padding: 10px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 5px;
            font-size: 16px;
            cursor: pointer;
        }

        .btn:hover {
            background-color: #45a049;
        }

        .footer {
            text-align: center;
            margin-top: 15px;
        }
    </style>
</head>
<body>

    <div class="login-container">
        <h2>Login</h2>
        <form action="" method="post"> <!-- Fixed form action -->

            <input type="text" name="username" class="input-field" placeholder="Username" required><br>
            
            <input type="password" name="password" class="input-field" placeholder="Password" required><br>

            <button type="submit" class="btn">Login</button>

        </form>
        <div class="footer">
            <p>Don't have an account? <a href="#">Sign up</a></p>
        </div> 
    </div>

    <?php if (!empty($error)) { echo "<p style='color:red; text-align:center;'>$error</p>"; } ?>

</body>
</html> 
