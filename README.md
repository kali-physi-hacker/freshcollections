# Fresh Collection Ecommerce Store


#### Brief Description
This project is an ecommerce store written in python with the Django Web Application
Framework. This project's main goal is to enable vendors place their products (items)
online and showcase of, thereby enabling end users (customers) purchase through this
app.
This app implements MTN Mobile Money (MOMO) Api so transactions can be made using MTN
MOMO.  
This app also implements the Paypal API for transactions as well
Api's are written with djangorestframework for the mobile version of this app.


#### Project Structure  
##### Apps
1. authentication
2. products
3. blog
4. apis

##### Models
1. User (Custom User Model) - authentication
2. Profile - authentication
3. Product - products
4. Blog - blog

##### URLconf
###### Authentication
```djangourlpath
- /authentication/ (main path)
```

```text
1. /login/                                      -       login (POST)
2. /logout/                                     -       logout (GET)
3. /auth/                                       -       login/register page (GET)
4. /register/                                   -       register (POST)
5. /register-success/                           -       register success page (GET)
6. /activate-user/<str:uidb64>/<str:token>/     -       activate user page (GET)
7. /activation-success/                         -       activation success page (GET)
8. /forgot-password/                            -       forgot password page / find your account (GET)
9. /reset-password/                             -       reset password page / Email password reset link (GET)
10. /change-password-page/                      -       change password page / Enter new password (GET)
11. /change-password/<int:pk>/                  -       change password (POST)
12. /profile/                                   -       Profile page (GET)
13. /update-user-profile/                       -       Update profile (POST)

```
<b>Note</b>  
Access to an endpoint (url)  
```text 
(domain)/authentication/auth/       -       for example visits the login/register page
```


#### Installation Guide 
In this guide, we'll be going through the following
steps in order to run this app
1. clone the project
2. move into the projects root directory
3. Do an environment based setup
4. Run server
#####  Step 1 & 2
```commandline
git clone https://github.com/estore.git
cd estore
```

#####  Step 3
With step three (3) you can either setup the project
up with Docker or a virtual environment
###### Docker
In the docker-compose.yml, there are three(3)
services going to be running. You can choose
which ever service to run all run all depending
on your preference. The services include:
1. dev          -       For development
2. stage        -       For staging
3. production   -       For production
```shell script
sudo docker build .
sudo docker-compose up
```
So depending on which service you would like 
to run, modify the second command above to
```shell script
sudo docker-compose up dev;  # Development
```
dev can be change to either of the following:
- stage
- production

###### Virtualenv
With the traditional virtualenv, you just need to  
1. create your virtual environment
2. activate it
3. install your dependencies (requirements)
4. run the app

```shell script
virtualen venv -p python3.8
source venv/bin/activate
pip install -r requirements.base
pip install -r requirements.dev
python manage.py runserver --settings=estore.settings.dev
```
Just as with the docker installation, depending on which environment you are 
setting up, replace requirements.dev as required.  
The following are the possible requirements file that can be used 
- requirements.dev
- requirements.stage
- requirements.prod

<b>Note:</b> that in all cases, it is required that you run installation for
requirements.base, as it a dependency for the other requirements.
