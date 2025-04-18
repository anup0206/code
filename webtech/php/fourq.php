<!DOCTYPE html>
<html>
<head>
    <title>Simple PHP Calculator</title>
</head>
<body>

<h2>Calculator</h2>
<form method="post" action="">
    <label>First Number:</label>
    <input type="number" name="num1" required><br><br>

    <label>Second Number:</label>
    <input type="number" name="num2" required><br><br>

    <label>Operator:</label>
    <select name="operator" required>
        <option value="+">+</option>
        <option value="-">-</option>
        <option value="*">*</option>
        <option value="/">/</option>
    </select><br><br>

    <input type="submit" name="calculate" value="Calculate">
</form>

<?php
if (isset($_POST['calculate'])) {
    $num1 = $_POST['num1'];
    $num2 = $_POST['num2'];
    $operator = $_POST['operator'];

    switch ($operator) {
        case "+":
            $result = $num1 + $num2;
            echo "<h3>Result: $num1 + $num2 = $result</h3>";
            break;
        case "-":
            $result = $num1 - $num2;
            echo "<h3>Result: $num1 - $num2 = $result</h3>";
            break;
        case "*":
            $result = $num1 * $num2;
            echo "<h3>Result: $num1 * $num2 = $result</h3>";
            break;
        case "/":
            if ($num2 == 0) {
                echo "<h3>Error: Division by zero!</h3>";
            } else {
                $result = $num1 / $num2;
                echo "<h3>Result: $num1 / $num2 = $result</h3>";
            }
            break;
        default:
            echo "<h3>Invalid operator!</h3>";
    }
}
?>

</body>
</html>