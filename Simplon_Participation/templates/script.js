// script.js

// Wait for the DOM to be fully loaded
document.addEventListener("DOMContentLoaded", function() {
  // Get the form element
  const form = document.querySelector("form");

  // Add an event listener for the form submission
  form.addEventListener("submit", function(event) {
    // Prevent the default form submission
    event.preventDefault();

    // Get the form inputs
    const nomInput = document.getElementById("nom");
    const prenomInput = document.getElementById("prenom");
    const telephoneInput = document.getElementById("telephone");
    const emailInput = document.getElementById("email");

    // Perform any desired operations with the form data
    const participantData = {
      nom: nomInput.value,
      prenom: prenomInput.value,
      telephone: telephoneInput.value,
      email: emailInput.value
    };

    // Example: Log the participant data to the console
    console.log(participantData);

    // You can add additional logic or make AJAX requests here
    // to process the participant data as needed
  });
});
