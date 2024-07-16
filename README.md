# E_commerce_project

E_commerce_project
This project resembles a basic E-commerce application but with different logic and implementation. It allows all users to perform basic operations like adding items to the cart, selecting the number of items to buy, searching for items, etc.

1. Implementation of Django REST-API
    - Any authenticated user can view the data associated with the application (primarily item-related data). However, to create, update, or delete data, the user must send POST, PUT, or DELETE requests.
      - To perform these operations, the user must be an Admin.
      - Admin users need an API KEY to proceed.
      - The application specifies the process in the API section, explaining everything about handling APIs.
2. Authentication and Authorization
    - This section is implemented using REST FRAMEWORK'S JWT TOKEN AUTHENTICATION.
       - Every user, upon logging in, will be provided with a JWT token. The process proceeds from there.
3. Database Interaction
   - As seen in the views section of the project, MySQL queries are used directly in the program to connect to the database.
       - This handles the inclusion of items into the database or the website.