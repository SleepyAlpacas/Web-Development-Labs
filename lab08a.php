<?php
$int1 = $_POST['int1'];
$int2 = $_POST['int2'];
if ($int1 < 3){
    echo "First number is less than 3";
}
elseif ($int1 > 12){
    echo "First number is greater than 12";
}
elseif ($int2 < 3){
    echo "Second number is less than 3";
}
elseif ($int2 > 12){
    echo "Second number is greater than 12";
}
else{
    echo "<table style='border:1px solid white;width:150px; height: 150px; background-color:black;'>";
    for ($i = 1; $i <= $int1; $i++){
        echo "<tr>";
        for ($i2 = 1; $i2 <= $int2; $i2++){
            $ans = $i2 * $i;
            echo <<<ABC
            <td style="border:1px solid white; color: yellow; font-family:'Comic Sans MS', 'Comic Sans', cursive; text-align: right;">$ans</td>
ABC;
        }
        echo "</tr>";
        //echo "<br>";
    }
    echo "</table>";
}
echo "<br>";
echo "<a href='lab08.php'>Go Back</a>";
?>