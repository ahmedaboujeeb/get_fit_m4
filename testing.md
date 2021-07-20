### This page includes all test cases done manually.


## Home Page

- The home page has clean easy instructions with sign up and login button button to access programs.
- Hero image shows with a nice clickable logo that takes you to home page.

### once logged in:

- A menue bar shows with options to click on that redirects to the respective page. 
- Click on the page you want to go to and you will be redirected with no issues.
- You will no longer have to the option to log in or sign up and the sign up button on the hero image will change to "My Programs" button that will redirect you to your purchased programs.
- a Logout option will show and will redirect you to confirm sign out page.

## Navbar

On mobile nave bar will be in a collapsible toggle. Click on toggle menue will expand.

- Click on Join Us will redirect you to sign up page.
- Click Login will redirect to login page.

### once logged in:

- Click on My Profile will take you to my profile page
- Click on Programs redirects you to program page to view our programs.
- Click on My programs redirects to your purchased programs to access.
- Click on Logout redirects you logout confirmation page.

As an Admin you will have a Program Management option, click on Program management redirects to add program page.

Users who don't have admin access will not have that option visible.

## Join us

- Fill in email address, confirm email address, username, password, confirm password all mandatory and will not be able to sign up if one or more fields is empty or doesn't fulfill all requirements.
- If username is taken a message will indicate that and a unique username needs to be chosen. 
- If password is weak, commom or similar to username a message will indicate that. 
- Click sign up, if all requirements fulfilled you will be signup and logged in and redirected to home page.

## Login

- Username and password are mandatory fields and will no be able to log in if one or both are incprrect and doesn't match. 
- A remember me box to be remembered on the device used.
- Click on Forgot Password redirects to reset password page.
- Click sign in, if all good redirects to home page as logged in user.

## Reset password page

-

## My profile

- Profile photo shwoing at the top in the middle of the page, with "no image available" photo if no image is added. 
- My billing information can be updated, none of the fields is mandatory. If you chose to save your billing info when completing checkout, informatio will be stored here.
- Click cancel if you do not wish to proceed with updating your information, and the page will refresh and the old information will be back. 
- My orders show your purchase history (order number, Program name, order date, price). If no orders have been made a message will indicate so.
- Click on program name redirects to program details page.

## Programs

- Shows our programs to ligged in visitors with program image, program name, a short description, price and a buy button in a card. 
- Click on Buy redirects to checkout page.
- If user has already purchased a program a "Go to program button" will show to avoid buying and already purchased program.
- Click on "Go to program" button redirects you to program details page.

Admin users:

- will have a "Edit" and "Delete" option next to Buy, click on edit redirects to edit program page. 
- Click on Delete, shows confirmation message if clicked yes program will be deleted. If program is already purchased by a user, program will not be deleted and error message will show.

## Checkout

- Fill in full name, email address, phone number, street address 1, town or city, country all mandatory and will not be able to complete order if one or more fields are empty or doesn't fulfill all requirements.
- Save my billing address check box if you wish to save information in profile. 
- Card number is mandatory and Stripe card check is done.
- Click Complete order, if all good it redirects to order completed page.

## Order Confirmation page

- A thank you message will show with program name, order ID, email address, and link to program details page.

## Confirmation email

- Is sent to users email address with order details.

## My programs

- Shows purchased programs for a logged in user.
- Program image, name, short description, status "paid" and "go to program" button will show. 
- Click on go to program redirects you to program details page.
- If no programs are purchased, a message will indicate so.

## Program details page

- Program name, image, full description, daily routine table will show in a nice, clean and easy to read order.
- admin users will have an edit and delete option. 

## Add program

- Only admin users have access to this page and are able to add programs, other users will not have access.
- All fields are mandatory (except for sku and image url) and program will not be added if one or more fields are empty or don't fulfill requirements.
- Click on add program, if all good it redirects to programs page. 
- Click on cancel redirects to home page.

## Edit Program

- Same as add programs, however fields will be filled with existing information. 
- Click on update program will update program.
- Click on cancel redirect to programs page. 

## Responsiveness

The design was tested using chrome devtools on the following devices:

- Responsive (Google Chrome dev tools).
- Moto G4
- Galaxy S5
- Pixel 2
- Pixel 2 XL
- Iphone 5/SE
- Iphone 6/7/8
- Iphone 6/7/8 Plus
- Iphone X
- Ipad
- Galaxy Fold
- Surface Duo
