
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Calculate Marks</title>
<body>
    <div class="form-container">

    <form method="post">
        <label for ="percentage">Percentage :</label>
        <input type="number" name="percentage" placeholder="Enter the percentage" required>
        <br><br>

        <button type="submit">calculate</button>
    </form>
    </div>

</body>
</html>
<?php 
    $percentage = $_POST['percentage'];
    if($percentage >100 || $percentage < 0 ){
        echo "Please enter the valid number !!!";
    } else{
        if($percentage >= 90)
            $grade = "A+";
        else if($percentage >80)
            $grade = "A";
        else if($percentage >70 )
            $grade = "B+";
        else if($percentage >60)
            $grade = "B";
        else
            $grade = "fail";

        echo "<p>Your percentage: $percentage</p>";
        echo "<p>Your grade: $grade</p>";
    }
 ?>

