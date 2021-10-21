# MS3 Movie collection

Movie collection is a website with movies based on books where people can find movies by books of different genres. That gives the opportunity to compare movie and book story. Movies have a link to watch them or link to buy a book for reading. Users also can share their favourite movies and books.

![mockup](https://github.com/Dynjashik/MSP3-Movie-collection/blob/master/static/images/README%20file/Mockup.png)

Live Website: [here.](https://my-milestone-project3.herokuapp.com/)

## Table of Contents
**[User Experience](#UX)** 

**[Features](#Features)**

**[Database schema](#Database)**

**[Technologies](#Technologies)**

**[Testing](#Testing)**

**[Deployment](#Deployment)**

**[Bugs](#Bugs)**

**[Credits](#Credits)**

## UX

This project is created for people who want to watch high quality movies based on books. Usually books inspire on good and deep movies. It’s also interesting for booklovers to look at a book story from a different angle and compare it with movie adaptation.

### User Stories

As a user I want to:
* Navigate through the website easily and clearly.
* Have an opportunity to view movies without registering an account.
* Get detailed information about each movie.
* Register and login to the website.
* Edit personal information when logged in.
* Add my own movies to the collection.
* Edit movies added by me.
* Delete movies added by me.
* Have an overview only on movies added by me.
* Filter movies by different categories.
* Search movies by name.

Additionaliy as an admin user I want to:
* Edit any movie in the collection.
* Delete any movie in the collection.
* Add movie categories.
* Delete movie categories.
* Have access to add affiliate links to each movie left by users, and earn money from those links.

### Strategy

The goal is to create a good quality list of movies to quickly find a suitable movie or book, to advertise books for people of all ages who like movies and books.

### Scope

Features that should be in the project:
* Navbar with menu and logo
* Home page with several recently added movies sorted by time added
* Movies page with movie collection
* Movie category filter 
* Search bar where movies can be found by category and by name with freetext
* Separate page for each movie with its details
* Sign In/Sign Up pages
* Add movie page for users who are logged in
* Edit movie page for users who are logged in
* Profile page where logged in user can edit personal information and view movies added by him.
* Admin user role that can add/delete movie categories and edit/delete any movie in the collection.
* Movie categories page that can be accessed only by admin
* Modal information messages for any changes on the website to communicate with a user
* Log out functonality


### Structure

All pages have a fixed navbar with main menu, logo and username of a user that is currently logged in.

The website has:
* A Home page with a banner, welcome message and recently added movies for all users
* A Movies page with all movies which can be filtered by category and movie name for all users
* Page with movie information for every movie in the list for all users
* Sign in and sign up pages for all users
* Profile page with user’s information and user’s movies where user can edit them.
* Add and edit movie page for registered users
* Manage categories page for the user Admin
* Edit, delete movie buttons
* Log out button

### Skeleton

Mockup of the website was created in ["Balsamiq Wireframes"](https://github.com/Dynjashik/MSP3-Movie-collection/blob/master/static/images/README%20file/MS%20Project%203.pdf).

### Surface

The design of website based on [material design base colors](https://materializecss.com/color.html) color style. 
For readability of the site a simple white background and black text were chosen.
Colors for home page and buttons:

* #26c6da cyan lighten-1 -  for buttons
* #00acc1 cyan darken-1 - for buttons
* #ffa726 orange lighten-1 -  for main menu

Background image on home page is taken from [here](https://lithub.com/the-best-literary-adaptations-to-stream-over-thanksgiving-break-or-right-now/).
To keep the design clean no other colors were used because of a lot of colorfull movie images.

Logo of the website in the navigation menu is created by Darya.

The font-family Tahoma, Verdana, sans-serif is used on the website because it has a narrower body, smaller counters, much tighter letter spacing, and a more complete Unicode character set. 

## Database 

[MongoDB](https://account.mongodb.com/account/login?n=%2Fv2%2F60ba880b16ccf0213a133e12%23metrics%2FreplicaSet%2F60e4469c9fc1390a86c8e35e%2Fexplorer%2FmyProject3%2Fusers%2Ffind) was used for this project and schema design was created. 

![img](https://github.com/Dynjashik/MSP3-Movie-collection/blob/master/static/images/README%20file/MongoDB%20diagram.png)

## Features

Existing Features

* Each page has a responsive and fixed to the top navigation menu. Menu items become active on currenlty opened pages. There is a logo in the center of navigation bar and a logged in username on the right.
* Home page has:
	* Background image with a website title.
	* Welcome message.
	* Three recently added movies.
* Movies page has:
	* List of all movie cards with images. Cards are clickable and all movie details can be revealed.
	* Search box where movies can be searched by category or title with freetext
	* Filter movies by category.
* Separate page for each movie with full information.
* Pages with sign in and sign up forms.

Signed in users have access to:
* Profile page with user’s information and user’s added movies. There is opportunity to update information and manage movies (edit, delete) on separate movie pages.
* Add movie form with input fields: movie name, category name, year, duration, description, movie link, book link, movie image link.
* Edit movie page to update movie information.
* Log out button
Admin user have access to:
* Manage categories page to add or delete movie categories.
* Manage all movies on the website to edit or delete them.

* All flash messages coming from Flask open in pop up window.
* Confirmation modals before deleting any information or updating user personal information.
* The password field uses Werkzeug to hash the password on entry and confirm password is validated using Javascript. 

### Features left to implement
* Footer with contact information so it is possible to contact developer
* Forgot password functionality
* Share movies in social networks
* Leave review to the movie
* Rate/Like movie

On mobile devices navigation bar menu transforms into a hamburger vertical menu.
Otherwise all other pages are the same.

## Technologies

### Database 

[MongoDB](https://www.mongodb.com/)

### Languages used:

HTML5 - for basic content and structure of the site. 
CSS3 - for design. 
Javascript - logic for the game. 
Python - for writing the scripts to render all the different templates using flask and connecting to mongodb. 

### Frameworks and libraries used:

[MaterializeCSS](https://materializecss.com/about.html)- for creating the responsive structure of the website, layout and design.  
[Flask](https://flask.palletsprojects.com/en/2.0.x/) - a python web framework.   
[PyMongo](https://pymongo.readthedocs.io/en/stable/) - python tool for use with Mongo DB. 
[JQuery](https://jquery.com/) - for making the site interactive.   
[Font Awesome](https://fontawesome.com/) - for using icons.  
[Google Fonts](https://fonts.google.com/) -  for font of the website.  
[Balsamiq](https://balsamiq.com/) - for creating the wireframe. 


### Tools and Other Resources used:

[Github](https://github.com/) - for version control and store the code for the project.   
[Gitpod](https://www.gitpod.io/) - for writing the code for the website and push it to Github.    
[Heroku](https://id.heroku.com/login) – for deployment the project.  
[Werkzeug](https://werkzeug.palletsprojects.com/en/2.0.x/) - for verifying the hashed password and username.  
[Dbdiagram](https://dbdiagram.io/home) - tool to draw database relationship diagrams and flow quickly using just keyboard.  
[Mockup generator](http://techsini.com/multi-mockup/index.php) - for testing responsive website on various devices.  
[W3 Schools](https://www.w3schools.com/) - for HTML, CSS, JS, Python tips.  
[Stackoverflow](stackoverflow.com) - for finding answers on questions.  
[Webformatter](https://webformatter.com) - for beautifying HTML, CSS, Javascript codes. 
[Datetime](https://docs.python.org/3/library/datetime.html#module-datetime) - for manipulating dates and times. 
[Regular expression](https://docs.python.org/3/library/re.html)- matching operations similar to those found in Perl. 

### Codes used:

Some of the code was taken from the sources:
* [Stackoverflow](https://stackoverflow.com/) - for setting a “created_by” field in all movies when changing username, for updating profile page, for styling movie cards and etc.
* [Onlinepngtools](https://onlinepngtools.com/create-transparent-png) – for creating transparent logo for the project.
* [CodeInstitute course](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+DCP101+2017_T3/courseware/9e2f12f5584e48acb3c29e9b0d7cc4fe/6449dcd23ca14016aa83dc7313d91a02/?child=first) – to custom code for Materialize select validation. 
* [Blog Teclado](https://blog.teclado.com/flashing-messages-with-flask/) - for flashing messages with Flask in modal.
* [Blog ImageKit](https://blog.imagekit.io/how-to-handle-loading-images-that-may-not-exist-on-your-website-92e6c3c6ea63) - for loading of images that may not exist.

## Testing

| Story / Feature                                                                                                                                                                                               | Action                                                                                                                                                                                                                                                                                                                              | Result |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
| Navigate through the website easily and clearly.                                                                                                                                                              | The site uses clear distinctive colors, user-friendly navigation menu on top of every page. All the menu entries have descriptive names and reflect the purpose of pages that they open.                                                                                                                                            | PASSED |
| Have an opportunity to view movies without registering an account.                                                                                                                                            | Clicked on "Movies" menu item. Got on page with all movies without logging in.                                                                                                                                                                                                                                                      | PASSED |
| Get detailed information about each movie.                                                                                                                                                                    | Clicked on movie image, got a sliding information window with movie details. Clicked on "Open" icon of a random movie. A new page opened with movie details.                                                                                                                                                                        | PASSED |
| Register and login to the website.                                                                                                                                                                            | Clicked on "Sign In/Sign Up" menu item. Then clicked on "Sign Up" link. Entered username, email and password. Got a confirmation popup that registration was successful. After got redirected to Sign in page. Entered my username and password and clicked "Sign in". After that got redirected to Home page with welcome message. | PASSED |
| Edit personal information when logged in.                                                                                                                                                                     | Clicked on "Profile" menu item while logged in. Personal information page opened. Changed my email and clicked "Update". Got a popup message with a message that my personal information is updated successfully. Opened Home page, then Profile page again and verified that the email changed.                                    | PASSED |
| Add my own movies to the collection.                                                                                                                                                                          | Clicked "Add movie" menu item while logged in. Filled in all the required fields, clicked "Add movie". Got redirected to Movies page and confirmation popup message showed. Found it in the movie grid.                                                                                                                             | PASSED |
| Edit movies added by me.                                                                                                                                                                                      |    Opened a movie detail page that was added by me. Clicked "Edit" button. Changed description and book link. Clicked "Submit". Got redirected to movie detail page with a confirmation popup window. Verified that description and book link changed accordingly.                                                                                                                                                                                                                                                                                                                             |  PASSED      |
| Delete movies added by me.                                                                                                                                                                                    |  Clicked "Delete" button on movie detail page that was added by me. Pressed "Yes" in confirmation pop up window. Got redirected to movie list page with a confirmation message that the movie was deleted successfully. Verified that it does not exist in the movie list.                                                                                                                                                                                                                                                                                                                                    |  PASSED      |
| Have an overview only of movies added by me.                                                                                                                                                                  | Clicked on "Profile" menu item while logged in. Personal information page opened. Found My Movies section below with all movies added by me.                                                                                                                                                                                        | PASSED |
| Filter movies by different categories.                                                                                                                                                                        | Clicked "Movies" menu item. Movies page opened and it has a list of clickable category buttons. Clicked "Comedy" category button. Only movies with Comedy category got shown.                                                                                                                                                       | PASSED |
| Search movies by name.                                                                                                                                                                                        | On Movies page there is a search on top center. Wrote "jungle" in input field and clicked search button. Only "The Jungle Book" movie appeared on the page. Wrote "documentary" in input field and clicked search button. Only movies with category Documentary got shown.                                                          | PASSED |
| Admin                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                                                                                     |        |
| Edit any movie in the collection.                                                                                                                                                                             | Logged in as admin. Opened Movies page and opened detail page of a random movie. Clicked "Edit" button below movie image. Changed year, category and name. Clicked "Submit". Got redirected to movie details page and confirmation popup message is shown. Verified that name, year and category changed correctly.                 | PASSED |
| Delete any movie in the collection.                                                                                                                                                                           |                                                                                                                                                                                                                                                                                                                                     |        |
| Add movie categories.                                                                                                                                                                                         |                                                                                                                                                                                                                                                                                                                                     |        |
| Delete movie categories.                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                     |        |
| Have access to add affiliate links to each movie left by users, and earn money from those links.                                                                                                              |                                                                                                                                                                                                                                                                                                                                     |        |
| Each page has a responsive and fixed to the top navigation menu.  Menu items become active on currenlty opened pages.  There is a logo in the center of navigation bar and a logged in username on the right. |                                                                                                                                                                                                                                                                                                                              

The following steps were taken to ensure the website works as intended:
* Ensure that all user stories are achieved:
	* Navigation through the website is easy and clear.
	* There is opportunity for all users to view the movie collection before logging in.
	* There is search bar in movie collection page where user can search with freetext for a movie by its name or category.
	* There is a category filter in movie collection.
	* Clickable movie cards with movie image that reveal detailed movie information.
	* There is a button to sign in and sign up in the menu.
	* There is button to add favourite movies in the menu.
	* The website has Profile page with ability to edit user’s information and view all movies added by the user.
	* Users can log out of the site securely.

	* User Admin has easy access to all areas of the website.
	* User Admin can edit or delete any movie.
	* User Admin can add or delete movie categories.

* Ensure that all features work well: 
	* Each page has a responsive and fixed to the top navigation menu. Menu items become active on currenlty opened pages. There is a logo in the center of navigation bar.
	* Navigation menu has Home, Movies and SignIn/SignUp buttons for not signed up users. Profile, Add Movie, Log Out for signed ip users. Additional button ”Manage categories” is for Admin user. There is a user’s name in the right corner of Menu.
	![img](https://github.com/Dynjashik/MSP3-Movie-collection/blob/master/static/images/README%20file/Menu.png)
	* Home Page is a main page and has a background image with a website title, welcome text and three recently added movies.
	![img](https://github.com/Dynjashik/MSP3-Movie-collection/blob/master/static/images/README%20file/Home_page.png)
	* Movies page has a list of all movie collection, search box of movies by category, by title, movie filter by category. 
	![img](https://github.com/Dynjashik/MSP3-Movie-collection/blob/master/static/images/README%20file/Movies_page.png)
	* Movies cards have a user’s or default image with title, details button. Clicking on card movie information with book link opens.
	  Clicking on details button a seprate movie page is opened with possibility to edit and delete it if the user logged in.
	![img](https://github.com/Dynjashik/MSP3-Movie-collection/blob/master/static/images/README%20file/Movie_card.png)
	* Clicking on SignIn/SignUp button SignIn form opens. If user hasn’t signed up there is a SignUp button that redirects to SignUp form. After signing in user is redirected to Home page.
	![img](https://github.com/Dynjashik/MSP3-Movie-collection/blob/master/static/images/README%20file/SignUp.png)
	* Profile page has signed in user’s information and user’s added movies with opportunity to update personal information and manage movies(edit, delete).
	![img](https://github.com/Dynjashik/MSP3-Movie-collection/blob/master/static/images/README%20file/Profile.png)
	* Add movie page has a form with input fields: movie name, category name, year, duration, description, movie link, book link, movie image link and submit button. 
	![img](https://github.com/Dynjashik/MSP3-Movie-collection/blob/master/static/images/README%20file/Add_movie.png)
	* On a separate movie page after there are "edit" and "delete" buttons if user created that movie. After clicking "edit" button, Edit Movie page opens with pre filled input fields. There are also ”submit” and ”back” buttons. "Back" button redirects to movie page without any changes.
	* Admin user has access to manage categories clicking on ”Manage Categoties” button in Menu. Also admin can manage (edit & delete) any movie on the website
	![img](https://github.com/Dynjashik/MSP3-Movie-collection/blob/master/static/images/README%20file/manage%20categories.png)
	* After any actions on the website such as signing in and signing up, add, edit and delete movie, update personal information, log out etc flash messages open in pop up windows with informative text or confirming question.
	* There are confirmatino modals before deleting any information.
	![img](https://github.com/Dynjashik/MSP3-Movie-collection/blob/master/static/images/README%20file/modal.png)
	* The password field uses Werkzeug to hash the password on entry and double confirm	password is validated using Javascript.

 * Ensure that all features work well on mobile version too:
     *All features on mobile version are the same.


The following online validators have been used for checking the code for any errors or warnings:
* [W3C HTML Validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmy-milestone-project3.herokuapp.com%2Fhome); 
 
There are no warnings or errors.

* [W3C CSS Validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fmy-milestone-project3.herokuapp.com%2Fhome&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en); 
 
There is 1 error and warnings connected to external libraries (MaterializeCSS, Awesome, hover.css) that I cannot access.

* [JShint](https://jshint.com/) looks good:  
![img](https://github.com/Dynjashik/MSP3-Movie-collection/blob/master/static/images/README%20file/Jshint.png)

Lighthouse testing was made in Chrome browser developer tools. 
* Desktop Lighthouse Improved Report:  
![img](https://github.com/Dynjashik/MSP3-Movie-collection/blob/master/static/images/README%20file/Lighthouse_desktop.png)

* Mobile Lighthouse Report:  
![img](https://github.com/Dynjashik/MSP3-Movie-collection/blob/master/static/images/README%20file/Lighthouse_mobile.png)
After testing the website with Mobile Lighthouse it was made improvement in CSS style to load CSS asynchronously.

The site was tested across different browsers and screen sized to validate responsiveness and browser compatibility.: Chrome, Internet Explorer, Safari, Firefox, UC Browser, Opera and Samsung Internet. It was also tested on mobile devices such as: iPhone Xs, iPhone 7, iPhone 11, Xiaomi Redmi Note 9. 

## Deployment

### Prerequisits & general steps

First follow these steps first before starting either local or remote deployment of the app.

* Create an acoount on [Gitpod](https://gitpod.io/). We will use it for both local and remote installations.
* Create an account om [Heroku](https://heroku.com/) for remote installation.
* Fork [this repository](https://github.com/Dynjashik/MSP3-Movie-collection) to your Github account.
* Open the forked repository using Gitpod like so: https://gitpod.io#<your_repository_url>

For testing purposes you can use my database, here are the configuration variables:
```
MONGO_DBNAME: myProject3
MONGO_URI: mongodb+srv://DaBel:Be1User@cluster0.zi7ip.mongodb.net/myProject3?retryWrites=true&w=majority
SECRET_KEY: <generated_key>
```

You can generate the key [here](https://miniwebtool.com/django-secret-key-generator/).

### Heroku

Steps for deploying the website to Heroku hosting platform:

* Login to Heroku, open Heroku Dashboard and Click _New -> Create new app_
* Enter appropriate app name and select the region closest to you.
* Open _Deploy_ tab and select Github as _Deployment method_. Connect your forked repository using the options below.
* Go to the _Settings_ tab, click _Reveal Config Vars_ in _Config Vars_ section.
* Add the following configuration variables:
```
IP : 0.0.0.0 
PORT : 5000
MONGO_DBNAME: <your_db_name>
SECRET_KEY:  <yout_db_secret_key>
MONGO_URI: <your_db_uri>
```
* Head back to the _Deploy_ tab in Heroku. Scroll down to _Automatic deploys_, click on _Enable Automatic Deploys_ and _Deploy Branch_.
* In _Manual deploy_ section click _Deploy Brach_.
* Go to _Activity_ tab to keep track when the app will be deoployed.
* After the app is deployed click _Open App_ to open the website.

### Gitpod
* In Gitpod create _env.py_ file in the root directory with the following content:
```
import os

os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("PORT", "5000")
os.environ.setdefault("SECRET_KEY", "<yout_db_secret_key>")
os.environ.setdefault("MONGO_URI", "<your_db_uri>")
os.environ.setdefault("MONGO_DBNAME", "<your_db_name>")
```

* Install project dependencies by running the following command in terminal:
```
pip install -r requirements.txt
```
* Start the app by typing following command:
```
python app.py
```
* Click _Open Browser_ in pop up message at bottom right corner.

## Bugs

During testing the project several bugs were fixed. Clicking on "Edit" button on Movie page the page was opening without logo of the website. To fix it I changed the path to logo image:"../../static/images/logo-icon.png".
![img](https://github.com/Dynjashik/MSP3-Movie-collection/blob/master/static/images/README%20file/bug.png)

Next bug was deleting random movie with a modal because of all delete modals had one id for all movies. It was fixed by adding unique id for each delete modal.

Other bug was on the Profile page with "Update" button. It didn't matter what it was chosen in confirming question, YES or NO, the information was updated in any case. The problem was solved by changing NO option from html tag <button> to <a> and href - on data-target with help of stackoverflow.com.

Next fixed bug was discovered with mentor when user updated any movie information, field "created by" became empty. Proplem was in code in file app.py. We should overwrite field "created_by" in db in app.route edit movie.

## Credits

### Contents

All content is written by developer Darya Belarusik.

### Media

Images for background, movie cards were taken from:

[pngtree](https://pngtree.com/freebackground/private-cinema-advertising-background_911781.html) - private Cinema Advertising Background that provides images for commrecial use.  
[LitHub](https://lithub.com/the-best-literary-adaptations-to-stream-over-thanksgiving-break-or-right-now/) - for background image on home page.

Logo of the website in navigation menu is created by Darya. 

### Acknowledgements

[Movies by books](https://www.bookbub.com/blog/best-movies-based-on-books-all-time) – inspiration for list of movies based on books.

Inspiration for this project was received from:
* Other code institute students' projects.
* Help of the mentor, slack and my husband.
