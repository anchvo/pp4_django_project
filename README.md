# Doc|Schedule
![Doc|Schedule](docs/docschedule.png)

Doc|Schedule is an online doctor appointment booking webpage with a special focus on senior citizens. It offers to register both Patients and Doctors to make booking appointments as easy as possible. 

The Live Website Link can be found here [Doc|Schedule](https://pp4-doctor-appointments-85bb5f1f4587.herokuapp.com/)

### Notes

For full testing purposes, I recommend setting up custom doctor and patient profiles to guarantee full functionality can be tested with all choice options.

## Contents

- [Requirements](#requirements)
- [UX](#ux)
    - [Project Goals](#project-goals)
    - [User Demographic](#user-demographic)
    - [User Experience](#user-experience)
    - [User Goals](#user-goals)
- [Development](#development)
    - [Database](#database)
    - [Wireframes](#wireframes)
- [Features](#features)
    - [Design](#design)
    - [Homepage](#home-page)
        - [Navbar](#navbar)
        - [Footer](#footer)
    - [User Registration & Profile Choice](#user-registration--profile-choice)
    - [Profile Setupt Forms](#profile-setup-forms)
    - [Profile Page](#profile-page)
    - [Create Appointment Form](#create-appointment-form)
    - [Manage Appointments Page](#manage-appointments-page)
    - [Edit Appointment Form](#edit-appointment-form)
    - [Delete Appointment Option](#delete-appointment-option)
    - [Sign In & Sign Out](#sign-in--sign-out)
    - [Error Page](#error-page)
- [Testing and Validation](#testing-and-validation)
- [Bugs](#bugs)
- [Technologies Used](#technologies-used)
    - [Libraries](#libraries)
- [Deployment](#deployment)
    - [GitHub](#github)
    - [Heroku](#heroku)
- [Future Updates](#future-updates)
- [Credits](#credits)
    - [Help, Advice and Inspiration](#help-advice-and-inspiration)
    - [Code](#code)
    - [Content](#content)

## Requirements

This website was created as the fourth required project for the Diploma in Full Stack Software Development from [Code Insitute](https://codeinstitute.net). 

Basic requirements:
  - A website with a SQL database connection
  - Working with Python & Django, Bootstrap
  - CRUD functionality
  - Agile Development
  - Documentation and deployment via GitHub
  - Deployment via Heroku 
  - Readme.md documentation
  - Manual and validator testing

## UX

### Project Goals

- Provide information about Doc|Schedule
- Provide Users with the ability to register / sign in / sign out
- Provide Users with the ability to create a profile
- Provide a database that stores data
- Provide actions with stored data
- Provide Users with the functionality to book and manage appointments

### User Demographic

This website is meant for:

- Users that are senior citizens and want to have an easy and straight-forward appointment booking system
- Users that are Doctors who want to offer their patients, especially senior citizens, the ability to book appointments with them online

### User Experience & User Goals 

Detailed User Stories were part of the agile development approach during this project and were set up via the GitHub Projects functionality.

The public Project Link can be found here [Doc|Schedule GitHub Project](https://github.com/users/anchvo/projects/1)

## Development

In the first developing stage, the general layout of the page was planned with the early decision to focus on styling the Layout with Bootstrap. 

### Database

For the database, a ERD was created to map out the general structure of the database models and their relationships. 
It was adjusted as needed during development to have a visualisation of the logic behind the database. 
Relationships were set up via OneToOne and ForeignKey to ensure data connectivity.

![ERD Model](docs/erdmodel.png)

The Model was created via account set up on [Eraser](https://www.eraser.io/)

### Wireframes

In the early development stages, wireframes were created to plan the overall structure and design of the webpage. Those wireframes were used as a guideline throughout the development process. Elements and design of the different pages were adjusted and added to while building the project, based on the original structure. The final project represents the early development ideas and goals.

![Wireframe Homepage](docs/wireframe_home.png)
![Wireframe Register Choice](docs/wireframe_register_choice.png)
![Wireframe Doctor Register](docs/wireframe_doctor_register.png)
![Wireframe Patient Register](docs/wireframe_patient_register.png)
![Wireframe Profile](docs/wireframe_profile.png)
![Wireframe Appointments](docs/wireframe_appointments.png)

The wireframes were created using [Figma](https://www.figma.com)

## Features

### Design

The design of the webpage was created with the user demographic in mind. It is supposed to be visually appealing for both patient and doctor users. 
Additionally, because the focus is on senior citizens, it was decided to create a more minimalistic design to ensure clarity of the content and user input.
In relation to the user demographic, the focus was also on creating the website with large screen design first and mobile second, as the assumption was made that most senior citizens prefer a large screen computer or laptop over a smartphone or smaller screen size.

The colour palette of the page is a subdued earth tones variants, to allow for enough contrast but forgo too intensive colours. 
The basic palette was inspired from [This Coolors Palette](https://coolors.co/palette/f0ead2-e7e8c4-dde5b6-c5d397-b9ca88-adc178-a98467-95755e-806755-6c584c) and slightly customised if needed.

The website also features different images. 
The first is the hero or landing image, that makes up most of the welcome / index page. It features the essential components of the website - a doctor & senior citizen talking via smartphone which lets the users relate to the site purpose immediately. 
Further images were used to create card images to let the users related to the written content. Card images were chosen for displaying reasons to use the website and for profile creation.
Images were custom created via [Canva](https://www.canva.com/).

### Home Page

- The home page is the first page the user sees when loading the website for the first time.
- It welcomes the user with a hero / landing image and a short welcoming message, explaining shortly what the site is about
- The welcome message also features Buttons that link to the register and sign in forms to allow for quick navigation should a user revisit the page
- Below the hero image are three content cards explaining what the page is about and what functionality and benefits the user can expect when using the page
- Images help to convey those messages

- The Home page includes the navbar and footer, which are set in the base.html and display the same on all subsequent pages: 

#### Navbar

- The navbar is located on the top of the page and includes page navigation links
- The left side is made up of the webpage brand consisting of the name Doc|Schedule in larger font and connected to a link to lead back to the home page when clicked
- When not logged in, the navbar displays links to the home page, the register form and sign in form to ensure access to all available site functions
- When logged in, the page displays links to the profile page instead of the home page, as this is the new main page for logged in users. It also displays the link to the sign out form. 
- When logged in, a user status option displays below the navbar, displaying a checked user icon and the users registered username to visualise the logged in status

#### Footer

- The footer contains contact information about the page fictional admins and creators that stand behind Doc|Schedule.
- Additionally, it contains information about the page creator / author and how to connect with them on GitHub and LinkedIn

[Screenshot Home Page](docs/docschedule.png)
[Screenshot Home Page Logged In](docs/docschedule_logged_in.png)

### User Registration & Profile Choice

- The User can register via a short register form and set up his username and password
- The register form is one of djangos account forms and was styled to fit the website design
- After registration, the user can choose between setting up a Patient or Doctor profile, visualised by images
- The user is given information about the functionality of each profile
- The user is then redirected to the respective form

### Profile Setup Forms

- The profile setup forms are the main user input forms for the database
- All user input is stored into the respective data models and can be accessed for later site functionality
- The user input differs depending on Patient or Doctor, as there are different requirements for each
- A Patient needs to enter basic profile data (name, email, phone) and set a preferred method of contact
- A Doctor needs to enter basic profile data (name, email, phone) as well as title, practice, specialisation, location, address and available features
- When submitting, the user is redirected to their profile page

### Profile Page

- The profile page is split into two cards, one showing the user profile, the other the next upcoming appointment based on date
- If no appointment is set up yet, the user is informed via a message on screen
- The profile page is connected to the user and profile role and displays information relating to that
- A user can only see their own profile data and appointments
- If the user is a Patient, the appointment information includes the corresponding Doctor data
- If the user is a Doctor, the appointment information includes the corresponding Patient data
- The next upcoming appointment view includes two buttons that redirect to further site functionality
- The Manage Appointments button redirects to the respective page
- The Create an Appointment button redirects to the respective form, but it is only visible to users with a patient profile to disable Doctor's from making appointments

### Create Appointment Form

- The create appointment form accesses the previously stored data from the profile setup forms
- It automatically connects to the user that accessed the button
- It allows the user to choose a Specialisation and Location and pick from a list of Doctors that fit those criteria
- If no Doctor fits the criteria, a notification informs the user about this and the list is empty
- The user can then pick the date and time of the appointment 
- The user can also add additional information that might be relevant to the appointment
- When submitting, the user is redirected to the manage appointments view

### Manage Appointments Page

- The manage appointments page shows a paginated view of all appointments connected to the user, sorted by next date
- The pagination allows to display six appointments at once before adding the option to display another page of appointments
- Like the profile view, each appointment includes information about it based on the user profile, Doctor or Patient
- Additionally, each appointment card has an edit appointment and delete appointment button
- The edit appointment button redirects the user to the edit appointment form, allowing to make changes to the respective appointment
- The delete appointment button should only be visible to patients and deletes the appointment when clicked

### Edit Appointment Form

- The edit appointment form accesses the previously stored data from the create appointment form
- It displays the same fields as the create appointment form but only allows editing of the date / time and additional info fields
- The contraints allow the users to update existing appointments that are also connected to related Doctors
- This means that the user cannot change the Location or Specialisation and therefore the Doctor as the chosen appointment is connected to a specific one
- The user is informed about what fields can be edited and referred to creating a new appointment should they wish to change the Doctor
- When submitting, the user is redirected to the manage appointments view

### Delete Appointment Option

- When a patient is logged in, the option to delete an appointment is available on the manage appointments page
- This allows patients to have more control over their appointments
- When clicking the delete appointment button, a modal is shown that asks for deletion confirmation to prevent accidental deletion
- When an appointment is deleted, the user is redirected to the manage appointments view and a message confirms the deletion

### Sign In & Sign Out

- The Sign in and Sign Out forms can be accessed from the navbar
- Depending on the logged status of the user, a different option can be chosen
- The Sign In option only shows for logged out users and refers to a django account form where the user can log in with their username and password
- The Sign Out option only shows for logged in users and refers to a django accoung form where the user has to confirm that he wants to log out

### Error Page

- A basic 404 error page is included in the webpage structure
- The page is loaded when a 404 error occurs
- The page shows an information that the error occured and suggests the user retrace their steps or contact the admins should the error persist

## Testing and Validation

The program has been tested and its code validated, the results can be viewed here: [Testing Documentation](https://github.com/anchvo/pp4_django_project/blob/main/testing.md)

## Bugs

## Technologies Used

Main: HTML, CSS, JavaScript, Python
Frameworks: Django, Bootstrap

IDE: VSCode

Websites:
- GitHub
- Code Institue Database Client
- Heroku

### Libraries

- The [Flatpickr](https://flatpickr.js.org/) for a better calender / date & time interface

## Deployment

### GitHub

-__On GitHub, the project was set up via the following steps:__

- Log in to GitHub and create repository
- Copy the provided code to set up project in VSCode
- Optional: fork or clone the repository by creating a new branch
- Use for version control during project creation by commiting and pushing code regularly
    - Remember to set `DEBUG` to `False` 
- Connect to Heroku to allow access to code

### Heroku

- __The website was deployed to Heroku via the following steps:__

- In code workspace, add necessary requirements to requirements.txt and Heroku to allowed Hosts
- Log in to Heroku and create new App
- In App settings, set the necessary _Config Vars_:
    - Key `COLLECTSTATIC` and value `TRUE`
- In Deployment tab, connect to GitHub
- Search for project on GitHub
- Deploy project
- In code workspace, set up necessary files to allow database connection
    - Procfile
    - .python-version 
- In App settings, set the necessary _Config Vars_:
    - Key `SECRET_KEY` and value `SECRETVALUE`
    - Key `DATABASE_URL` and value `DATABASEVALUE`
    & remove 
    - Key `COLLECTSTATIC` and value `TRUE`
- Redeploy to set up with database connection
- Redeploy constantly during project development


## Future Updates

- Enhance booking functionality by adding appointment slots and adding defensive coding to avoid double booking
- Add Contact form functionality to add another way to connect users and site admin
- Enhance Accessibility by adding options to enlarge font on screen 
- Add user tooltips to better explain site functionality
- Add better defensive coding to create a better and safer user experience

## Credits

### Help, Advice and Inspiration

- Jubril Akolade - my mentor
- Roman from tutor support

### Code

- Trouble-Shooting for bugs and learning about additional code options was assissted by using [W3Schools](https://www.w3schools.com/), [MDN Web Docs](https://developer.mozilla.org/en-US/), [Stack Overflow](https://stackoverflow.com/questions), Google Searches
- Official Documentation for Libraries and Frameworks was used to assist with code writing and functionality.
- Code Snippets for the general set up of the navbar, footer and card functionality were taken and customised from the [Code Institute Codestar Blog Walkthrough Project](https://github.com/Code-Institute-Solutions/blog/tree/main/01_getting_set_up/01_create_project_app)

### Content

- Most of the current content on the page is imaginary and was randomly created
    - Doctor and Patient information
    - Addresses, phone numbers & emails
    - Appointments
- Locations represent real cities but are not connected to any real doctors at that location
- As the website creator, the links to my social profiles are real and added to allow connecting with site visitors

