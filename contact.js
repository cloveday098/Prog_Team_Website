function sendMail(){
        var params = {
            name: document.getElementById("name").value,
            email: document.getElementById("email").value,
            phone: document.getElementById("phone").value,
            message: document.getElementById("message").value,
        };
        const serviceID = "service_5gas2ij";
        const templateID = "template_4h4llp7";

        emailjs.send(serviceID, templateID, params)
        .then(
            res =>{
                document.getElementById("name").value = "";
                document.getElementById("email").value = "";
                document.getElementById("phone").value = "";
                document.getElementById("message").value = "";
                console.log(res);
                alert("Your message was sent successfully!");
            }
        )
        .catch(err=>console.log(err));
    }