
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

        <button type="submit">calculate</button>
    </form>
    </div>

</body>
</html>
<?php 
    $percentage = $_POST['percentage'];
    if($percentage >100 ){
        if($percentage < 0){
            echo "Please enter the valid number !!!";
        }
    }
    else{
        if($percentage >= 90){
            echo "Youhave scored A+";
        }
        elseif($percentage >80 || $percentage <90){
            echo "Youhave scored A";
        }
        elseif($percentage >70 || $percentage < 80){
            echo "Youhave scored B+";
        }
        elseif($percentage >60 || $percentage < 70){
            echo "Youhave scored B";
        }
        else {
            echo"You are fail";

        }
    }
    
 ?>

