# Testing

## Contents

- [Manual Testing](#manual-testing)
- [Browser Testing](#browser-testing)
- [Database Testing](#database-testing)
- [Python Validation](#python-validation)
- [JavaScript Validation](#javascript-validation)
- [CSS Validation](#css-validation)
- [HTML Validation](#html-validation)

## Manual Testing

The following tests were carried out manually to ensure the portal is working correctly

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Home Page | User lands on the home page | Home page renders correctly | Works as expected |
| Navbar Logged Out | User sees the navbar when logged out | Navbar shows up with correct links | Works as expected |
| Navbar Logged In | User sees the navbar when logged in | Navbar shows up with correct links | Works as expected |
| Navbar Links | User is redirected from navbar links | Navbar links all work correctly | Works as expected |
| Navbar Toggle | User can use a navbar toggle on small screens | Navbar toggles on small screens | Works as expected |
| Home Page Images | User sees all images on the home page | Images are loaded correctly | Works as expected |
| Home Page Content | User sees all text content on the home page | Text content is loaded correctly | Works as expected |
| Home Page Register Button | User sees and can use the register button on home page | Button loads and redirects correctly | Works as expected |
| Home Page Sign In Button | User sees and can use the sign in button on home page | Button loads and redirects correctly | Works as expected |
| Footer | User sees the footer | Footer shows up with content | Works as expected |
| Base HTML Extension | User sees the same navbar and footer on all pages | Navbar and Footer load on all pages | Works as expected |
| User Status | User sees a status icon and username when logged in underneath navbar | User Status loads when user logs in | Works as expected |
| Register Form | User can register with a username and password | Register Form renders and submits correctly | Works as expected |
| Sign In Form | User can sign in with his username and password | Sign In Form renders and submits correctly | Works as expected |
| Sign Out Form | User can sign out | Sign Out Form renders and submits correctly | Works as expected |
| Profile Choice Page | User can choose to create a patient or doctor profile | Profile Choice Page renders correctly | Works as expected |
| Profile Choice Page | User is redirected to either the patient or doctor profile setup form | Profile Choice Page buttons redirect correctly | Works as expected |
| Doctor Profile Form | User can setup a doctor profile form | Doctor Profile Form renders and submits correctly | Works as expected |
| Doctor Profile Form Validation | User is reminded of required fields and data input restrictions | Doctor Profile Form Validation loads correctly | Works as expected |
| Patient Profile Form | User can setup a patient profile form | Patient Profile Form renders and submits correctly | Works as expected |
| Patient Profile Form Validation | User is reminded of required fields and data input restrictions | Patient Profile Form Validation loads correctly | Works as expected |
| Profile Page | User can see their profile and appointment information | Profile Page renders correctly | Works as expected |
| Profile Page Restrictions | User can only see profile and appointment information related to their user account | Profile Page restrictions restrict access | Works as expected |
| Profile Page Appointment | User can see their next upcoming appointment | Profile Page Appointment renders the next upcoming appointment correctly | Works as expected |
| Create Appointment Button | User can see create appointment button if they are a patient | Create Appointment button displays for patient profile only | Works as expected |
| Create Appointment Button | User (patient) is redirected to create appointment form  | Create Appointment button redirects correctly | Works as expected |
| Create Appointment Form | User can create and appointment | Create Appointment Form renders and submits correctly | Works as expected |
| Create Appointment Form Validation | User is reminded of required fields and data input restrictions | Create Appointment Validation loads correctly | Works as expected |
| Create Appointment Form Dynamic Filtering | User can choose a doctor that fits their previous selection criteria| Create Appointment Form Dynamic Filtering populates the doctor field based on user selection criteria | Works as expected |
| Manage Appointments Button | User can see manage appointments button | Manage Appointments button displays for all users | Works as expected |
| Manage Appointments Button | User is redirected to appointments page | Manage Appointments button redirects correctly | Works as expected |
| Appointments Page | User can see all their appointments | Appointment page renders correctly | Works as expected |
| Appointments Page Restriction | User can only appointments related to their user account | Appointment Page restrictions restrict access | Works as expected |
| Pagination | User can see six appointments at a time before new page is needed | Pagination displays up to six items at a time before offering redirect to next page | Works as expected |
| Appointments Page Restriction | User can only appointments related to their user account | Appointment Page restrictions restrict access | Works as expected |
| Create Appointment Button | User can see create appointment button if they are a patient | Create Appointment button displays for patient profile only | Works as expected |
| Create Appointment Button | User (patient) is redirected to create appointment form  | Create Appointment button redirects correctly | Works as expected |
| Edit Appointment Button | User can see edit appointment button | Edit Appointment button displays for users | Works as expected |
| Edit Appointment Button | User is redirected to Edit Appointment Form | Edit Appointment button redirects correctly | Works as expected |
| Edit Appointment Form | User can edit their appointment | Edit Appointment Form renders and submits correctly | Works as expected |
| Edit Appointment Form Restrictions | User can only edit the date/time and additional information of their appointment | Edit Appointment Form Validation loads correctly | Works as expected |
| Delete Appointment Button | User can see create appointment button if they are a patient | Create Appointment button displays for patient profile only | Works as expected |
| Delete Appointment Button | User can delete their appointment | Delete Appointment Button correctly deletes the appointment from the database | Works as expected |
| Delete Appointment Button User Confirmation | User has to confirm appointment deletion | User Confirmation modal loads and asks for confirmation | Does not work |
| Phone User Input Restriction | User can only enter phone number in specific formats | User Input for phone numbers is restricted and validated to ensure correct input | Works as expected |
| Date Input Restriction | User can not pick a date that is in the past | User Input for date / time is restricted and validated to ensure correct input | Works as expected |


## Browser Testing
The program was tested in the following browsers by myself and others: 

- Firefox 
- Brave
- Safari

It worked without issues in the above browsers

## Database Testing
The Database was accessed with the admin account and all database models show up correctly. User accounts can also be accessed correctly. 

## Python Validation
All Python Files have been passed through the [CI PEP8 Python Linter](https://pep8ci.herokuapp.com/) and returned no errors except E501 line too long

## JavaScript Validation
All JavaScript code has been passed through the [JSHint Validator](https://jshint.com/) and returned the general error E501 line too long, along with: 
Two Unused Variables : confirmDeleteHandler and main, which is expected and relates to the above mentioned error with the modal not loading

## CSS Validation
All CSS code has been passed through the [Jigsaw Validator](https://jigsaw.w3.org/css-validator/) and returned no errors.

## HTML Validation
All HTML code has been passed through the [W3C validator](https://validator.w3.org/) and returned no errors.