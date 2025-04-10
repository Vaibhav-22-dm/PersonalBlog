﻿# PersonalBlog

## About the Project
This is a django app made for an assignment of an internship selection process [9Island Technologies].
In this django app I have created an API which rotates the page of an an input file, saves the modified pdf and return the url of the pdf.

## Installation 

To install the following app on your local system follow the steps given below:

- Install Python 3.10.7
- Install virtualenv
- Create a folder by whatever name your want to give. Example: 9IslandTechnologies
- Open the 9IslandTechnologies folder in VS Code. Open the terminal.
- Create a virtual environment: 
    ```
    virtualenv myenv
    ```
- Switch to the newly created environment:
    ```
    cd myenv/Scripts
    ```
    ```
    ./activate
    ```
- Return Back to the parent directory:
    ```
    cd ../../
    ```
- Clone the repository:
    ```
    git clone https://github.com/Vaibhav-22-dm/PersonalBlog.git
    ```
- Change directory to newly cloned repository:
    ```
    cd PersonalBlog
    ```
- Build the environment using the given requirements:
    ```
    pip install -r requirements.txt
    ```

- Start the django server:
    ```
    python manage.py runserver
    ```

- Install the thunderclient extension on VS Code or use Postman to test the API:

    APIs:

    | url | response |
    | --- | -------- |
    | http://127.0.0.1:8000/blogs/getblogs/ | webpage with list of blogs |
    | http://127.0.0.1:8000/blogs/getblog/pk/ | webpage with blog having id = pk |
    | http://127.0.0.1:8000/admin/ | webpage with login form |

- Following are credentials of multiple users to login and edit the blogs:
    | username | password |
    | -------- | -------- |
    | sandip1712 | tudu2171 |
    | vaibhav@blogs | mohite@123 |

- To add new users login with superuser credentials :
    | username | password |
    | -------- | -------- |
    | admin | admin |
    
    - Go to users table.
    - Click on Add User.
    - Enter valid username and password.
    - Click on Save
    - Add the First Name, Last Name and Email of the newly created user.
    - In the User Permissions field add the following permissions:
        - Blogs | blog | Can view blog
        - Blogs | blog | Can change blog
        - Blogs | blog | Can add blog
    - Save the changes.

- To add a blog, login to the admin panel using your credentials and click on add blog.

