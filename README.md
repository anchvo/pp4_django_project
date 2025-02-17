# Title
![Doc|Schedule](docs/docschedule.png)

Doc|Schedule is an online doctor appointment booking webpage with a special focus on senior citizens. It offers to register both Patients and Doctors to make booking appointments as easy as possible. 

The Live Website Link can be found here [Doc|Schedule](https://pp4-doctor-appointments-85bb5f1f4587.herokuapp.com/)

### Notes

## Contents

- [Requirements](#requirements)
- [UX](#ux)
    - [Project Goals](#project-goals)
    - [User Demographic](#user-demographic)
    - [User Experience](#user-experience)
    - [User Goals](#user-goals)
- [Development](#development)
- [Database](#database)
- [Features](#features)
    - [Feature 1](#feature-one)
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

## Features

### Design

The design of the webpage was created with the user demographic in mind. It is supposed to be visually appealing for both patient and doctor users. 
Additionally, because the focus is on senior citizens, it was decided to create a more minimalistic design to ensure clarity of the content and user input.

The colour palette of the page is a subdued earth tones variants, to allow for enough contrast but forgo too intensive colours. 
The basic palette was inspired from [This Coolors Palette](https://coolors.co/palette/f0ead2-e7e8c4-dde5b6-c5d397-b9ca88-adc178-a98467-95755e-806755-6c584c) and slightly customised if needed.

The website also features different images. 
The first is the hero or landing image, that makes up most of the welcome / index page. It features the essential components of the website - a doctor & senior citizen talking via smartphone which lets the users relate to the site purpose immediately. 
Further images were used to create card images to let the users related to the written content. Card images were chosen for displaying reasons to use the website and for profile creation.
Images were custom created via [Canva](https://www.canva.com/).

### Home Page

### Navbar

### Footer

### User Registration & Profile Setup

### Profile View

### Manage Appointments View

### Sign Out & Sign In 

### Error Page

## Testing and Validation

The program has been tested and its code validated, the results can be viewed here [TESTING](https://github.com/anchvo/pp4_django_project/blob/main/testing.md)

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
- Official Documentation was used for Code creation: 
- Code Snippets for the general set up of the navbar, footer and card functionality were taken and customised from the [Code Institute Codestar Blog Walkthrough Project](https://github.com/Code-Institute-Solutions/blog/tree/main/01_getting_set_up/01_create_project_app)

### Content

- Most of the current content on the page is imaginary and was randomly created
    - Doctor and Patient information
    - Addresses, phone numbers & emails
    - Appointments
- Locations represent real cities but are not connected to any real doctors at that location
- As the website creator, the links to my social profiles are real and added to allow connecting with site visitors

