function sendmail() {
var email = document.getElementsByClassName("emailId");
var message = document.getElementsByClassName("message");
var request = new XMLHttpRequest();
var url = "../sarath-sattiraju/php/sendMail.php";
    
request.open("POST",url,true);
request.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");

request.onreadystatechange = function() {
    if(this.readyState == 4 && this.status == 200) {
        alert("Success!");
    }
};
request.send("email="+email+"&message="+message);
}
