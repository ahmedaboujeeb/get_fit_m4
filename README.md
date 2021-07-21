# GET FIT

[Link to live website.](https://getfit-m4.herokuapp.com/)

## User Experience (UX)

### User Stories

#### First time visitor goals

##### As a first time visitor I wan to:

- be able to easily navigate throughout the site to find content from any device.
- be able to sign up for a new account easly.
- be able to access fitness programs after logging in.
- be able to purchase fitness programs.

#### Returning visitor goals

##### As a returning visitor I wan to:

- be able to access purchased programs.
- be able to update my billing information.
- be able to reset password.
- be able to update profile pictures.
- be able to view purchase history.

#### Frequent visitor goals

##### As a frequent visitor I wan to:

- check if there is any newly added fitness programs.

## Design

A simple design easy to navigate for first time and returning visitors of all ages, with simple black, white and grey colors. 

[Link to Wireframs](https://github.com/ahmedaboujeeb/get_fit_m4/blob/main/get_fit_wireframes.pdf)

## Features

- Responsive design that works perfectly on any on any device.
- Fully functioning navbar that adapts to small screens with a collapsable toggle.
- Sign up and log in functionality. 
- Sign up confirmation email. 
- Ability to reset password. 
- Access to program list only after signup and login. 
- Ability to purchase a program.
- Confirmation email after purchase completed.
- Access program only if paid. 
- View order history.
- Update billing information.
- Upload/update profile photo.
- Access purchased program list.

## Technologies Used

- Programming languages: HTML, CSS, JavaScript, Python.
- Frameworks/libraries: Bootstrap, Django, Jquery.
- Database: Sqlite3, PostgresSQL.
- Version control: Git was used for version control to commit to Git and Push to GitHub.
- Payments: Stripe used to process payments.
- Static and media files host: AWS S3 bucket
- Emails: Gmail used to send confirmation emails.
- Deployemnt: Heroku used to deploy the live version, GitHub used to store the projects code after being pushed from Git.
- IDE: VS Code used to  code the website.
- Fonts: Google fonts used for fonts accross the website.
- Wireframes: Balsamiq was used to create the wireframes.

## Testing

The W3C Markup Validator, W3C CSS Validator, jshint JS validator and pep8online Python validator services were used to validate every page of the project to ensure there were no syntax errors in the project.

[Link to UX test cases](https://github.com/ahmedaboujeeb/get_fit_m4/blob/main/testing.md)

## Deployment

This website is deployed to Heroku and the repository is hotsted on GitHub. 

What you need to deploy this project is:

- IDE
- Python3, PIP and Git 
- Stripe Account
- AWS Account and S3 bucket
- Heroku Account
- Gmail Account

### Local deployment

#### GitHub

[Link to main repository](https://github.com/ahmedaboujeeb/get_fit_m4)

To make a local clone:

1. Log in to GitHub and locate the main repository.
2. Click in the code buttin at the top of the page.
3. Clone the repository using HTTPS by copying the URL.
4. Open terminal in your IDE.
5. CHange current work directory to preferred location.
6. Type git clone and past the URL https://github.com/ahmedaboujeeb/get_fit_m4.git
7. Type pip3 install -r requirements.txt in terminal
8. Setup the environment variables. This process is different depending on the used IDE. The following variables are needed:
DEVELOPMENT=True
STRIPE_PUBLIC_KEY = <YOUR STRIPE_PUBLIC_KEY>
STRIPE_SECRET_KEY = <YOUR STRIPE_SECRET_KEY>
STRIPE_WH_SECRET = <YOUR STRIPE_WH_SECRET>
10. Create a database and migrate the models by typing the following commands in terminal: 'python3 manage.py makemigrations' -> 'python3 manage.py migrate'. 
11. Create a super user to access django admin panel with the following command: 'python3 manage.py createsuperuser' you will then be asked for an email address, username and password.
12. you can start the website locally by typing this commcand 'python3 manage.py runserver'.

### Heroku deployment

1. Create a Heroku account and log in. 
2. Create a new app.
3. Install Heroku Add-on Heroku Postgres from the resources tab. The free Hobby Dev version is enough - click the provision button to add it to your project.
4. Create requirements.txt from your project with the help of 'pip3 freeze --local > requirements.txt'.
5. Create a Procfile echo web: gunicorn puffins.wsgi:application > Procfile
6. Commit changes and push to.
7. Set the environment variables in Heroku Settings > Reveal Config Variables The following Variables must be set: USE_AWS = TRUE
AWS_ACCESS_KEY_ID = <YOUR AWS_ACCESS_KEY_ID>
AWS_SECRET_ACCESS_KEY = <YOUR AWS_SECRET_ACCESS_KEY>
DATABASE_URL = <YOUR DATABASE_URL> (Set by Heroku Postgres)
EMAIL_HOST_USER = <YOUR EMAIL_HOST_USER>
EMAIL_HOST_PASSWORD = <YOUR EMAIL_HOST_PASSWORD>
DEFAULT_FROM_EMAIL = <YOUR DEFAULT_FROM_EMAIL>
STRIPE_PUBLIC_KEY = <YOUR STRIPE_PUBLIC_KEY>
STRIPE_SECRET_KEY = <YOUR STRIPE_SECRET_KEY>
STRIPE_WH_SECRET = <YOUR STRIPE_WH_SECRET>
USE_AWS = True
8. Copy the DATABASE_URL and set it up in your IDE (make sure you keep secret and don't commit it).
9. To test if the Postgres database is connected to your IDE you can make use of the command python3 manage.py showmigrations. This should show undone migrations for all models.
10. Migrate models.
11. Create a new super user.
12. Log in to Heroku from terminal.
13. Add existing repository to Heroku 'heroku git:clone -a <your repository>'.
14. Push to Heoku 'git push heroku master'.
15. Create a S3 bucket on AWS. The bucket should contain a folder called static. To upload the product images create a new folder called media, and add the files to folder. Make sure to give public read access to objects.

## Credits

- Some features were inspired by Code Institute Boutique Ado project.
- Toasts and toast styling were taken from Boutique ado.

### Media

- Hero image and program images were downloaded from https://www.pexels.com/
- Navbar and other features were taken from https://getbootstrap.com/
