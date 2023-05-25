const studentForm = document.getElementById("student-form");

let students;
let tmp;
if(studentForm)
{
  studentForm.addEventListener("submit", (event) => {
    let isValid = validateStudentForm();
    if (!isValid) {
     event.preventDefault();
      window.scrollTo(0, 0);
    }
  });
}

function validateStudentForm() {
  let isValidForm = false;
  let studentNameInput = document.getElementById("student-name");
  let studentEmailInput = document.getElementById("email");
  let studentPhoneInput = document.getElementById("phone");
  let studentIdInput = document.getElementById("student-id");
  let studentGpaInput = document.getElementById("gpa");
  let studentLevelInput = document.getElementById("level");
  let studentDepartmentInput = document.getElementById("department");
  let studentNationalIdInput = document.getElementById("national-id");
  let studentNationalityInput = document.getElementById("nationality");
  let studentGender = document.getElementsByName("gender");
  let studentStatus = document.getElementsByName("status");
  let studentDateOfBirthInput = document.getElementById("date-of-birth");
 
  let isValidName = validateName(studentNameInput);
  showFeedback("Student name should be at least three words", studentNameInput, isValidName);

  let isValidId = validateId(studentIdInput);
  showFeedback("ID should be exactly 8 digits", studentIdInput, isValidId);

  let isValidEmail = validateEmail(studentEmailInput);
  showFeedback("Email should be in a valid format, e.g. name@example.com", studentEmailInput, isValidEmail);

  let isValidPhone = validatePhone(studentPhoneInput);
  showFeedback("Phone number should be 11 digits and start with 01", studentPhoneInput, isValidPhone);

  let isvalidGender = validateGender(studentGender);
  showFeedback("Gender should be selected", studentGender[0].parentElement.parentElement, isvalidGender);

  let isValidStatus = validateStatus(studentStatus);
  showFeedback("Status should be selected", studentStatus[0].parentElement.parentElement, isValidStatus);

  let isValidLevel = validateLevel(studentLevelInput);
  showFeedback("Level should be selected", studentLevelInput, isValidLevel);

  let isValidDepartment = validateDepartment(studentDepartmentInput);
  showFeedback("Department should be selected", studentDepartmentInput, isValidDepartment);

  let isValidGpa = validateGpa(studentGpaInput);
  showFeedback("GPA should be between 0 and 4.00", studentGpaInput, isValidGpa);

  let isValidNationalId = validateNationalId(studentNationalIdInput);
  showFeedback("National ID should be valid", studentNationalIdInput, isValidNationalId);

  let isValidNationality = validateNationality(studentNationalityInput);
  showFeedback("Nationality should be selected", studentNationalityInput, isValidNationality);

  let isvalidDateOfBirth = vaildateDateOfBirth(studentDateOfBirthInput);
  showFeedback("Date of birth should be selected", studentDateOfBirthInput, isvalidDateOfBirth);

  if (isValidName && isValidId && isValidEmail && isValidPhone && isvalidGender && isValidStatus  && isValidLevel && isValidDepartment && isValidGpa &&
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

const levelInput = document.getElementById("level");
if (levelInput) {
  levelInput.addEventListener("input", handleDepartmentOptions);
}


function handleDepartmentOptions() {
  let departmentInput = document.getElementById("department");

  if (levelInput.value > 2) {
    for (let i = 0; i < departmentInput.options.length; i++) {
      departmentInput.options[i].style.display = "block";
    }
  } else {
    departmentInput.selectedIndex = 0;
    for (let i = 2; i < departmentInput.options.length; i++) {
      departmentInput.options[i].style.display = "none";
    }
  }
}
function hideDepartmentOptions() {
    let departmentInput = document.getElementById("department");
      departmentInput.selectedIndex = 0;
  
    for (let i = 2; i < departmentInput.options.length; i++) {
        departmentInput.options[i].style.display = 'none';
    }
  }

 