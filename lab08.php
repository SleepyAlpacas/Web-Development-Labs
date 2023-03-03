<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body style="margin:0">
    <h1>QUESTION 1</h1>
    <?php
    $background;
    $message;
    if (date("h") >= 6 && date("h") < 12){
        $background="background-image:url('https://images.freeimages.com/images/large-previews/a1b/the-sun-1396604.jpg');";
        $message="Good Morning";
    }
    elseif (date("h") >= 12 && date("h") < 18){
        $background="background-image:url('https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/A_good_afternoon_%286933189752%29.jpg/1200px-A_good_afternoon_%286933189752%29.jpg');";
        $message="Good Afternoon";
    }
    elseif (date("h") >=18 && date("h") < 24){
        $background="background-image:url('https://thumbs.dreamstime.com/b/evenning-background-same-plants-tree-one-sun-colour-yellow-tree-colour-green-sky-bule-evening-wallpapers-100112866.jpg');";
        $message="Good Evening";
    }
    else{
        $background="background-image:url('https://metaverse386798621.files.wordpress.com/2021/04/mac-tonight.png');";
        $message="Good Night";
    }
    echo <<<ABC
    <div style="$background height:500px; background-size:cover; margin:0;">
    <h1 style="color:lime;font-size:100px;">$message</h1></div>
ABC;
    setcookie('numVisits', $_COOKIE['numVisits'] + 1, time()  + 60*60*24*14);
    
    if ($_GET['image']){
        $image;
        if ($_GET['image'] == 'pumpkin'){
            $image='https://ihypress.com/holidays/halloween/jacklantern2.gif';
        }
        elseif($_GET['image'] == 'skeleton'){
            $image="https://ihypress.com/holidays/halloween/skeldance.gif";
        }
        elseif($_GET['image'] == 'broom'){
            $image="https://ihypress.com/holidays/halloween/broom.gif";
        }
        echo "<img src=$image style='position:fixed; top:0px; right:0px; opacity:50%;'>";
    }

    
    ?>
    <?php
    $temp = $_COOKIE['numVisits']+1;
    echo <<<ABC
    <p style="position:fixed; bottom:10px; right:5px;">Number of Visits: $temp</p>
ABC;
    //https://ihypress.com/holidays/halloween/jacklantern2.gif
    //https://ihypress.com/holidays/halloween/skeldance.gif
    //https://ihypress.com/holidays/halloween/broom.gif
    ?>
    <h1>QUESTION 2 </h2>
    <form action="lab08a.php" method="post">
        <label>Enter 2 Integers</label>
        <br>
        <input type="text" name="int1">
        <br>
        <input type="text" name="int2">
        <input type="submit">
    </form>

</body>
</html>