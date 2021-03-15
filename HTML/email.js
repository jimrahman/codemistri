contactForm = document.getElementById("contact_form");
contactForm.onsubmit = (element) => {
  element.preventDefault();

  name = document.getElementById("name").value;
  email = document.getElementById("email").value;
  phone = document.getElementById("phone").value;
  message = document.getElementById("message").value;

  raw = JSON.stringify({
    name: name,
    email: email,
    subject: phone,
    message: message,
  });
  console.log(raw); 

  fetch("http://127.0.0.1:5000/contact", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: raw,
    redirect: "follow",
  })
    .then((response) => response.text())
    .then((result) => {
      console.log(result);
      if (result == "received") {
        alert("Your message has been sent");
      } else {
        alert("Sorry we couldn't send your message, please try again");
      }
    })
    .catch((error) => console.log("error", error));
};
