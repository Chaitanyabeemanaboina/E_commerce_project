# E_commerce_project
- This project resembles a Basic E_commerce application but the logic and implementation are completely different, which allows all the user to perform basic operations, like adding items to cart, selecting number of items to buy,search for items etc..
- Implementation of Django REST-API:
  - Any Authenticated user can view the data associated with the application (basically the data related to items),but when he wants to create, update or delete data he should send a POST,PUT,DELETE requests.
    In order to do that a user has to be a Admin user. Assuming that he is a Admin user, he needs an API KEY to move forward.
    The application specifies the process in the API section, which explains everything about the handling of API's.
- Authentication and Authorization:
  - This section is implemented using REST FRAMEWORK'S JWT TOKEN AUTHENTICATION. Every user when logs in ,will be provided a jwt token from there on the process proceeds.
- As you have seen in the views section of the project we have used Mysql Queries , directly in the program to connect to the database.
 this handles inclusion of items into the database or the website.