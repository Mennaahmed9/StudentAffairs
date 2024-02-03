# StudentAffairs
This project is a Student Affairs website  built in Django.The website allows users to manage student information, courses, and course registrations. Users can add, update, and delete student data, view active/inactive students, search for students by name. The website also includes a login functionality for user authentication.

# Functionalities
## 1- Add New Student:
Users can effortlessly add new students by providing key details such as ID, name, date of birth, GPA, gender, level, status (active/inactive), department, email, and mobile number.
## 2- Update Student Information:
Editing existing student information is made easy, with the department field disabled for editing to maintain data accuracy.
## 3- Delete Student Data:
The system incorporates a delete button on the edit student data page, prompting a confirmation dialogue before permanently removing student records.
## 4- Search for Active Students:
Users can quickly search for active students by name, with the results presented in a user-friendly table format for easy reference.
## 5- Assign Department to a Student:
After searching for a specific student, users can assign a department through the dedicated department assignment page. This feature is accessible only for students with a level of 3, with clear error messages for ineligible cases.
# 6- View All Active/Inactive Students:
Separate pages display tables containing information about all active or inactive students, showcasing relevant attributes for quick reference.
## 7- Change Student Status:
Administrators can conveniently switch a student's status from active to inactive or vice versa directly from the table displaying all students.
## 8- Well-Designed Navigation: 
The website boasts a well-crafted navigation bar, allowing users to effortlessly explore different pages, ensuring a smooth and intuitive user experience.

# Technologies Used
The Student Affairs website is built using the following technologies:
** Django **
** HTML **
** CSS ** 
** JavaScript **

## Getting Started

To run this project locally, follow these steps:

1. Clone the repository:
```
git clone https://github.com/Mennaahmed9/StudentAffairs.git
```

2. Navigate to the project directory: 
```cd project_directory```

3. Set up a virtual environment: 

- On Windows:
```
python -m venv env
```
```
env\Scripts\activate
```
  
- On macOS and Linux:

```
python3 -m venv env
```
```
source env/bin/activate
```
  
4. Install project dependencies:
```
cd studentAffairs
```
```

pip install -r requirements.txt
```

5. Run: 
```
python manage.py runserver
```
  
  
