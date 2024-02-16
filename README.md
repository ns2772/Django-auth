# Django Custom User With allauth

```
A Django Website in which include custom user model with django-allauth setup and
template are available in bootstrap 5.
```

`` Authentication Supported Services ``
* Email & Password With Verification

## Usage

First clone this repo
```bash
git clone https://github.com/ns2772/Django-Assessment.git 
```

Create a `.env` file
```bash
touch mysite/.env
```

Place your credentials in `.env` file
```bash
DEBUG=True
SECRET_KEY=your-secret-key
```

Create A virtualenv
```bash
virtualenv env
```

Build the Docker Container
```bash
docker-compose build
```

Run the Docker Container:
```bash
docker-compose up
```

Admin login credentials:
```bash
admin@example.com
```
```bash
User@123
```

## Implementation Details

### Made a login app using Django's Auth that consists of a custom user model named "CustomUser".

### Tech: Python, Django, SQLite, CSS, Boostrap 5 and Docker. 

### Details:
- Docker Containerization of app. Built my own Dockerfile and use docker-compose to `up` the system.
- User Registration
    > No duplicate users
- Login Interface
    > Once User Accesses System Allow them to Edit thier Account as a secure page.
- Create a custom template tag that shows the last time a user logged in, using local timezone when rendered. 
- 2FA based on Email for both signup and login. 
- Forgot password functionality (you can use password hints or email based reset).
- Logout  
- Give the user an option to change the color scheme of the site permantently by choice.
- Allow the user to change the timezone by selection for the custom template tag

