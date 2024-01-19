<?php
    $name = $email = $phone = $message = $nameErr = $emailErr = $phoneErr = $msgError = "";
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
      if (!isset($_POST['name'])) {
        $nameErr = "Please enter a valid name";
      }
      else {
        $name = get_input($_POST["name"]);
        if (!preg_match("/^[a-zA-Z-' ]/", $name)) {$nameErr = "Only letters and whitespace allowed!";}
      }

      if (isset($_POST['email'])) {
        $email = get_input($_POST["email"]);
        if (!preg_match("/^[a-zA-Z-' @]/", $email)) {$emailErr = "Only letters, @, and whitespace allowed!";}
      }
      else {$emailErr = "Email cannot be empty!";}
      
      if (isset($_POST['phone'])) {
        $phone = get_input($_POST["phone"]);
        if (!preg_match("/^[0-9-() ]/", $phone)) {$phoneErr = "Give a valid phone number!";}
      }
      else {$phoneErr = "Give a valid phone number!";}

      if (isset($_POST['message']) && strlen(get_input($_POST["message"])) >= 5) {$message = get_input($_POST["message"]) . "<br>My phone number is ". $phone;}
      else {$msgErr = "Message must be at least 5 characters!";}
    }

    function get_input($data) {
      $data = htmlspecialchars($data);
      return $data;
  }
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Us</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" 
    integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

    <style>
      body {
          margin: 0;
          padding: 0;
          font-family: 'Poppins', sans-serif;
          color:#600015;
      }
      .error {
        color: #FF0000;
        background-color: inherit;
        border: transparent;
    }
      .custom-bg {
          background-color: #640928;
          color: #ff6500;
      }

      .custom-btn {
          background-color: #ff6500;
          color: #fff;
      }

      .custom-form-bg{
          background-color: rgba(58, 59, 64, 0.372);
          border-radius:4px;
      }
    </style>
<!--
<script src="contact.js"></script>
<script type="text/javascript"
    src="https://cdn.jsdelivr.net/npm/@emailjs/browser@3/dist/email.min.js">
</script>-->
<script type="text/javascript">
   /*(function(){
      emailjs.init("ogf2JF9JdcQbhnvuy");
   })();*/
   function test() {
        if (document.getElementById("name").value != "" &&
            document.getElementById("email").value != "" &&
            document.getElementById("email").value.search(/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/) != -1 &&
            document.getElementById("phone").value != "" &&
            document.getElementById("phone").value.search(/[a-zA-Z._!@#$%^&*+]/g) == -1 &&
            document.getElementById("message").value != "" &&
            document.getElementById("message").value.length >= 5) {
            
            document.getElementById('form1').submit();
            alert("Your message was sent successfully!");
        }
        else {   // Find out how to use regexs.
            alert("Error: Fill out all fields");
            if (document.getElementById("name").value == "") {document.getElementById("nameErr").value = "Please enter a valid name";}
            else {document.getElementById("nameErr").value = "";}

            if (document.getElementById("email").value == "") {document.getElementById("emailErr").value = "Email cannot be empty";}
            else if (document.getElementById("email").value.search(/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/) == -1) {document.getElementById("emailErr").value = "Include an actual email";}
            else {document.getElementById("emailErr").value = "";}
            
            if (document.getElementById("phone").value == "") {document.getElementById("phoneErr").value = "Phone cannot be empty";}
            else if (document.getElementById("phone").value.search(/[a-zA-Z._!@#$%^&*+]/g) != -1) {document.getElementById("phoneErr").value = "Enter a valid phone number";}
            else {document.getElementById("phoneErr").value = "";}
            
            if (document.getElementById("message").value.length < 5) {document.getElementById("msgErr").value = "Minimum 5 characters";}
            else {document.getElementById("msgErr").value = "";}
        }
        /*if (document.getElementById("nameErr").value == "" && document.getElementById("emailErr").value == "" && document.getElementById("phoneErr").value == "" && document.getElementById("msgErr").value == "") {
            //sendMail();
            alert(document.getElementById("name").value);
        }*/
        //alert(document.getElementById("nameErr").value);
   }
</script>
</head>
<!--<a href="file:///C:\Users\k12jsti\source\repos\Prog_Team_Website\home.html" style="float:left;"><img src="https://www.maryvillecollege.edu/wp-content/uploads/Images/Main/global/MC_V1-Enclosed_RGB_FullColor.png" width=auto height="50"></a>-->

<body style="background-color:lightsalmon;">
    <div class="container border mt-3 bg-red">
        <div class="row">
            <div class="col-md-6 p-5 custom-bg text-orange">
                <center><h1>Hello there!</h1></center>
                <h4>Feel free to contact us anytime if you have any questions. If you want to join or have suggestions, please send us your ideas.</h4>
            </div>
            <div class="col-md-6 py-3 custom-form-bg">
            <h1><center>Contact Form</center></h1> <!--fec31366a72fd21c2ebb7d88160a2d44 for chance.loveday-->   <!--366a6380303826f3d77a363358bfc3ae for programming.team-->
            <form id="form1" name="form1" action="https://formsubmit.co/366a6380303826f3d77a363358bfc3ae" method="POST">
                <input type="hidden" name="_subject" value="New Email">
                <input type="hidden" name="_next" value="http://localhost/contactthankyou.html">
                <input type="hidden" name="_captcha" value="false">
                <div class="form-group">
                    <h5 for="name">Name <span class = "error">* <input class="error" type="text" id="nameErr" value="" readonly></span> </h5>
                    <input type="text" class="form-control" id="name" name="name" placeholder="Enter your name" required>
                </div>
                <div class="form-group">
                    <h5 for="email">Email <span class = "error">* <input class="error" type="text" id="emailErr" value="" readonly></span> </h5>
                    <input type="email" class="form-control" id="email" name="email" placeholder="Enter your email" required>
                </div>
                <div class="form-group">
                    <h5 for="phone">Phone <span class = "error">* <input class="error" type="text" id="phoneErr" value="" readonly></span> </h5>
                    <input type="text" class="form-control" id="phone" name="phone" placeholder="Enter your phone number" required>
                </div>
                <div class="form-group">
                    <h5 for="message">Message <span class = "error">* <input class="error" type="text" id="msgErr" value="" readonly></span> </h5>
                    <textarea type="text" id="message" name="message" rows="3" class="form-control"></textarea>
                </div>
                <!--<input type='hidden' id='nameErr' value=<?php echo $nameErr;?>>
                <input type='hidden' id='emailErr' value=<?php echo $emailErr;?>>
                <input type='hidden' id='phoneErr' value=<?php echo $phoneErr;?>>
                <input type='hidden' id='msgErr' value=<?php echo $msgErr;?>>-->
                
            </form>
            <center><button type='submit' onclick="test()" class="btn custom-btn">Submit</button></center>
                
            </div>
        </div>
    </div>
</body>
</html>