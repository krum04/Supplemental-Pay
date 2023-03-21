const form = document.querySelector('form'); // select the form element
const firstNameInput = document.getElementById('employee-fname'); // select the first name input element
const lastNameInput = document.getElementById('employee-lname'); // select the last name input element
const idInput = document.getElementById('employee-id'); // select the ID input element
const submitButton = document.getElementById('submit'); // select the submit button element

// Disable the submit button initially
submitButton.disabled = true;

// Add event listeners to all required input fields
firstNameInput.addEventListener('input', validateForm);
lastNameInput.addEventListener('input', validateForm);
idInput.addEventListener('input', validateForm);

function validateForm() {
  if (firstNameInput.value.trim() !== '' && lastNameInput.value.trim() !== '' && idInput.value.trim() !== '') {
    // Enable the submit button when all required fields are completed
    submitButton.disabled = false;
  } else {
    // Disable the submit button when any of the required fields are empty
    submitButton.disabled = true;
  }
}
