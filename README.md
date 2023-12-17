# LeaderEdu

## Project README


## Project Overview

        This education management system is a comprehensive solution that encompasses various modules such as enrollment, courses, results, user authentication with JWT (JSON Web Token), teachers, categories, custom  users, and result tracking. Each module is designed with full CRUD (Create, Read, Update, Delete) operations, providing a robust system for managing educational processes.

## Modules

        1. Enrolment Module
        The enrolment module allows users to enroll in courses, providing a streamlined process for managing student registrations and course assignments.

        2. Courses Module
        The courses module facilitates the creation, management, and organization of academic courses. It  includes functionalities for adding new courses, updating existing ones, viewing course details, and    deleting courses.

        3. Results Module
        The results module is designed to track and manage student results. It provides features for inputting  grades,  generating result reports, and updating or deleting results.

        4. User Authentication Module with JWT
        The user authentication module handles user registration, login, and logout functionalities using JSON Web Tokens (JWT). It ensures secure access to the system and manages user accounts. Additionally, it supports password change and provides endpoints for obtaining access and refresh tokens.

        5. Social Authentication
        The project supports social authentication with Google, allowing users to sign up and log in using their Google credentials.

        6. Teachers Module
        The teachers module focuses on the management of teaching staff. It allows the addition of new teachers, updates to existing teacher profiles, viewing teacher details, and deleting teachers.

        7. Category Module
        The category module categorizes courses into different groups or subjects. It helps in organizing and structuring the courses based on their content or purpose. Users can create, update, view, and delete categories.

        8. Custom User Module
        The custom user module extends the default user model to include additional fields and functionalities. It allows for a more personalized user experience with features such as customizable profiles. Users can view, update, and delete their profiles.


## JWT Authentication

        This project uses JWT (JSON Web Token) authentication to secure user access. JWT tokens are issued upon successful login and should be included in the headers of subsequent requests for authenticated endpoints. Endpoints for password change, token retrieval, and user information are available.

        Social Authentication
        Users can sign up and log in using their Google credentials through the implemented social authentication system.


## Installation


        1.git clone <repository_url>
        2.pip install -r requirements.txt
        3.python manage.py migrate
        4.python manage.py createsuperuser
        5.python manage.py runserver
        6.Access the admin panel at http://127.0.0.1:8000/admin/ and log in with the superuser credentials.


## USAGE

## Enrolment:

        Navigate to the enrolment module to enroll students in courses.
## Courses:

        Use the courses module to create, update, view, and delete academic courses.
## Results:

        Access the results module to input student grades,  generate result reports, and update or delete results.
## User Authentication (JWT):

        Register new users, log in, and log out using the user authentication module with JWT. Include the JWT token in the headers for authenticated requests. Use password change endpoints for updating passwords.
## Social Authentication (Google):

        Users can sign up and log in using their Google credentials through the implemented social authentication system.
## Teachers:

        Manage teaching staff by adding new teachers, updating profiles, viewing details, and deleting teachers.
## Category:

        Organize courses by creating, updating, viewing, and deleting categories.
## Custom User:

        Customize user profiles by viewing, updating, and deleting their profiles.
        Contributing