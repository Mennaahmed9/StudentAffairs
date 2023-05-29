function editStudent() {
        // Get form data and id
        const studentId = document.getElementById("id").value;

        const form = document.getElementById("edit-form");
        const formData = new FormData(form);
    
    // let isValid = validateStudentForm();
   
    

        // Create an empty object to store the form data
        const payload = {};

        // Populate the form data object with key-value pairs
        for (let entry of formData.entries()) {
          payload[entry[0]] = entry[1];
        }

        // Send the AJAX request
        const xhr = new XMLHttpRequest();
        xhr.open("POST", "/update_student_info/" + studentId + "/");
        xhr.setRequestHeader("Content-Type", "application/json");
        xhr.onload = function () {
          if (xhr.status === 200) {
            const response = JSON.parse(xhr.responseText);
            console.log(response.message);
            alert(response.message);
          } else {
            console.error("Error:", xhr.status);
          }
        };
        xhr.onerror = function () {
          console.error("Network Error");
        };
        xhr.send(JSON.stringify(payload));
      }

      function deleteStudent() {
        const studentId = document.getElementById("id").value;
        console.log(studentId);
        const xhr = new XMLHttpRequest();
        xhr.open("DELETE", "/delete_student/" + studentId + "/");
        xhr.setRequestHeader("Content-Type", "application/json");
        xhr.onload = function () {
          if (xhr.status === 200) {
            const response = JSON.parse(xhr.responseText);
            alert(response.message);
          } else {
            alert("Delete student failed!");
            console.error("Error:", xhr.status);
          }
        };
        xhr.onerror = function () {
          console.error("Network Error");
          alert("Error!");
        };
        xhr.send();
      }
    
const studentForm = document.getElementById("edit-form");

let students;
let tmp;




function validateEditForm()
{
  let isValidForm = false;
  const studentNameInput = document.getElementById("edit-name");
  const studentEmailInput = document.getElementById("edit-email");
  const studentPhoneInput = document.getElementById("edit-phone");
  const studentGpaInput = document.getElementById("edit-gpa");
  const studentLevelInput = document.getElementById("edit-level");
  const studentNationalIdInput = document.getElementById("edit-national-id");
  const studentNationalityInput = document.getElementById("edit-nationality");
  const studentDateOfBirthInput = document.getElementById("edit-date-of-birth");

  let isValidName = validateName(studentNameInput);
  showFeedback("Student name should be at least three words", studentNameInput, isValidName);

  let isValidEmail = validateEmail(studentEmailInput);
  showFeedback("Email should be in a valid format, e.g. name@example.com", studentEmailInput, isValidEmail);

  let isValidPhone = validatePhone(studentPhoneInput);
  showFeedback("Phone number should be 11 digits and start with 01", studentPhoneInput, isValidPhone);

  let isValidLevel = validateLevel(studentLevelInput);
  showFeedback("Please select level", studentLevelInput, isValidLevel);

  let isValidGpa = validateGpa(studentGpaInput);
  showFeedback("GPA should be between 0 and 4.00", studentGpaInput, isValidGpa);

  let isValidNationalId = validateNationalId(studentNationalIdInput);
  showFeedback("National ID should be valid", studentNationalIdInput, isValidNationalId);

  let isValidNationality = validateNationality(studentNationalityInput);
  showFeedback("Nationality should be selected", studentNationalityInput, isValidNationality);
  
    let isvalidDateOfBirth = vaildateDateOfBirth(studentDateOfBirthInput);
  showFeedback("Date of birth should be selected", studentDateOfBirthInput, isvalidDateOfBirth);

  if (isValidName  && isValidEmail && isValidPhone   && isValidLevel  && isValidGpa &&
      isValidNationalId && isValidNationality && isvalidDateOfBirth)
  {
    isValidForm = true;
  }
  
  return isValidForm;
}


function showFeedback(message, element, isValidInput) {
  if (!isValidInput) {
      displayError(element, message);
    }
      
    else {
      hideError(element);
    }
}

const displayError = (div, message) => {
  const errorElement = div.nextElementSibling;
  errorElement.innerHTML = '<i class="material-icons">error</i> ' + message;
  
  if(!(div.classList.contains("radio-container")))
    div.style.border = "1px solid red";
  else {
    let labels = div.getElementsByTagName("label");

    labels[0].style.color = "red";
    labels[1].style.color = "red";
  }
  
}

const hideError = (div) =>{
  const errorElement = div.nextElementSibling;
  errorElement.innerText = "";

 if(!(div.classList.contains("radio-container")))
   div.style.border = "none";
  else {
   let labels = div.getElementsByTagName("label");
    labels[0].style.color = "white";
    labels[1].style.color = "white";
  }
}

const validateName = (name) => {
    const nameValue = name.value.trim();
    const nameRegex = /^[a-zA-Z]+([ ][a-zA-Z]+){2,}$/;

  return nameRegex.test(nameValue);
}

const validateId = (id) => {
  const idValue = id.value.trim();
  const idRegex = /^[0-9]{8}$/;

  return idRegex.test(idValue);
}

const validateEmail = (email) => {
  const emailValue = email.value.trim();
  const emailRegex = /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/;

  return emailRegex.test(emailValue);
}
const validatePhone = (phone) => {
  const phoneValue = phone.value.trim();
  const phoneRegex = /^01[0125][0-9]{8}$/;
  
  return phoneRegex.test(phoneValue);
}

const validateGender = (gender) => {
  for (let i = 0; i < gender.length; i++) {
    if(gender[i].checked)
      return true;
  }
  return false;
}

const validateStatus = (status) => {
  for (let i = 0; i < status.length; i++) {
    if(status[i].checked)
      return true;
  }
  return false;
}

const validateLevel = (level) => {
  return (level.selectedIndex !== 0);
}

const validateDepartment = (department) => {
  return (department.selectedIndex !== 0);
}

const validateGpa = (gpa) => {
  const gpaValue = gpa.value.trim();
  const gpaRegex = /^(4(\.0{1,2})?|[0-3](\.[0-9]{1,2})?)$/;

  return gpaRegex.test(gpaValue);
}

const validateNationalId = (nationalId) => {
  return (nationalId.value.trim().length !== 0);
}

const validateNationality = (nationality) => {
  return  (nationality.selectedIndex !== 0);
}

const vaildateDateOfBirth = (dateOfBirth) => {
  return (dateOfBirth.value.length !== 0);
}






 