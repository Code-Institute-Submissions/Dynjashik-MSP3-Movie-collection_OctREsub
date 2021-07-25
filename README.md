# MS3 Movies collection

Movies collection is a website with a list of movies based on books where people can find movies by books of different genres that gives the opportunity to compare movie and book story. Movies have a link to watch them or link to buy a book for reading. Users also can recommend their favourite movies and books.

![mockup](https://github.com/Dynjashik/MSP3-Movie-collection/blob/master/static/images/README%20file/Mockup.png)

Live Website: [here.](https://my-milestone-project3.herokuapp.com/)

## Table of Contents
**[User Experience](#UX)** 

**[Features](#Features)**

**[Database schema](#Database schema)**

**[Technologies](#Technologies)**

**[Testing](#Testing)**

**[Deployment](#Deployment)**

**[Bugs](#Bugs)**

**[Credits](#Credits)**

## UX

This project is created for people who want to watch high quality movies based on books  because books inspire on good and deep movies. It’s also interesting for booklovers to look at a book story with a different look and compare it with movie adaptation.

### User Stories

As a user I want to:
* Navigate through the website easily and clearly.
* Have an opportunity to view the movie collection before registering an account.
* Read movie information with movie links for watching and book links for purchasing them.
* Clearly Sign In/Sign Up on the page.
* Have a possibility to edit personal information.
* Have an ability and motivation to add their own movie examples.
* Have a possibility to edit and delete posted movies.
* Search movies by different categories and by the name.
* Filter movie collection by category.
* Securely log out of the site.

As Admin I want to:
* Give easy entrance to all areas of the site.
* Have an ability to add, edit and delete any movie.
* Be able to manage movie categories.
* Have access to add affiliate links to each movie left by a user, and earn money from those links.

### Strategy

The goal is to create a good quality list of movies to quickly find a suitable movie or book, to advertise books for people of all ages who like movies and books.

### Scope

Features that should be in the project:
* Navbar with menu and logo
* Three recently added movies on home page
* Movie page with movie collection with their description
* Filter by category
* Search movies by category and by name
* Sign In/Sign Up forms for user
* Add movie page for users signed up/in
* Edit form and delete movie function with confirmation modal
* Edit personal information for user on profile page
* Add movie category function for Admin
* Flash messages
* Log out


### Structure

The website has:
* A Home page with navbar menu, logo and recently added movie examples for all users
* A Movies page with all movies which can be filtered by category for all users
* Page with movie information for every movie in the list for all users
* Sign in and sign up pages for all users
* Profile page with user’s information and user’s movies where user can edit them.
* Add and edit movie page for registered users
* Manage categories page for the user Admin
* Edit, delete movie buttons
* Log out button

### Skeleton

Mockup of the website was created in ["Balsamiq Wireframes"]().

### Surface

The design of website based on [material design base colors](https://materializecss.com/color.html) color style. 
For readability of the site a simple white background and black text were choosen which are defined with used colors for home page and buttons:
* #26c6da cyan lighten-1 -  for buttons
* #ffa726 orange lighten-1 -  for main menu
Background image on home page are taken [here](https://lithub.com/the-best-literary-adaptations-to-stream-over-thanksgiving-break-or-right-now/).
To keep the design clean no other colors were used because of a lot of colorfull movie images.

Logo of the website at the navigation menu is created by Darya.

The font-family size  Tahoma, Verdana, sans-serif is used on the website because of it has a narrower body, smaller counters, much tighter letter spacing, and a more complete Unicode character set. 

##Database schema
[MongoDB](https://account.mongodb.com/account/login?n=%2Fv2%2F60ba880b16ccf0213a133e12%23metrics%2FreplicaSet%2F60e4469c9fc1390a86c8e35e%2Fexplorer%2FmyProject3%2Fusers%2Ffind) was used for this project and schema design was created. 
![img](https://github.com/Dynjashik/MSP3-Movie-collection/blob/master/static/images/README%20file/MongoDB%20diagram.png)

## Features

Existing Features

* Each page has a responsive and fixed to the top navigation menu with active button to the current page link and with logo of website.
* Home Page has:
	** Background image with a website title.
	** Three recently added movies.
* Movies page has:
	** List of all movies cards with images, movie information, links and information about creator.
	** Search box of movies by category, by title.
	** Filter movies by category.
* Movie page with one selected movie with full information.
* Page with sign in and sign up forms for users.
Signed in users have access to:
* Profile page with user’s information and user’s added movies. There is opportunity to update information and manage movies(edit, delete).
* Add movie form with input fields: movie name, dropdown category name, year, duration description, movie and book link, optional movie image.
* Edit movie page to update movie information.
* Log out button
Admin user have access to:
* Manage categories page to add or delete movie categories.
* Manage all movies on the website to edit or delete them.
* Log out button

* All flash messages open in pop up window.
* Confirmation modals before deleting any information.
* The password field uses Werkzeug to hash the password on entry and confirm password is validated using Javascript. 

### Features left to implement
* Footer with contact information with opportunity to connect with developer
* Email for retrieving a forgotten password.
* Share movies in social links
* Leave review of movies

On mobile devices all pages are the same.

## Technologies

### Database

[MongoDB[(https://www.mongodb.com/)

### Languages used:

HTML5 - for basic content and structure of the site.
CSS3 - for design.
Javascript - logic for the game.
Python - for writing the scripts to render all the different templates using flask. And connecting to mongodb

### Frameworks and libraries used:

[MaterializeCSS](https://materializecss.com/about.html)- for creating the responsive structure of the website, layout and design. 
[Flask](https://flask.palletsprojects.com/en/2.0.x/) - a python web framework
PyMongo() - 
[JQuery](https://jquery.com/) - for making the site interactive.
[Font Awesome](https://fontawesome.com/) - for using icons.
[Google Fonts](https://fonts.google.com/) -  for font of the website.
[Balsamiq](https://balsamiq.com/) - for creating the wireframe.

### Tools and Other Resources used:

[Github](https://github.com/) - for version control and store the code for the project.
[Gitpod](https://www.gitpod.io/) - for writing the code for the website and push it to Github.
[Heroku](https://id.heroku.com/login) – for deployment the project.
[PyMongo](https://pymongo.readthedocs.io/en/stable/) - python tool for use with Mongo DB.
[Werkzeug](https://werkzeug.palletsprojects.com/en/2.0.x/) - for verifying the hashed password and username.
[Dbdiagram](https://dbdiagram.io/home) - tool to draw database relationship diagrams and flow quickly using just keyboard. 
[Mockup generator](http://techsini.com/multi-mockup/index.php) - for testing responsive website on various devices.
[W3 Schools](https://www.w3schools.com/) - for HTML, CSS, JS, Python tips.
[Stackoverflow](stackoverflow.com) - for finding answers on questions.
[Webformatter](https://webformatter.com) - for beautifying HTML, CSS, Javascript codes.

### Codes used:

Some of the code for the game was taken from the sources:
* [Stackoverflow](https://stackoverflow.com/questions/2450954/how-to-randomize-shuffle-a-javascript-array) - for shuffling game cards.
* [Onlinepngtools](https://onlinepngtools.com/create-transparent-png) – for creating transparent logo for the project.
* [CodeInstitute course](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+DCP101+2017_T3/courseware/9e2f12f5584e48acb3c29e9b0d7cc4fe/6449dcd23ca14016aa83dc7313d91a02/?child=first) – to custom code for Materialize select validation 

## Testing

The following steps were taken to ensure the website works as intended:
* Ensure that all user stories are achieved:
	* Navigation through the website is easy and clear.
	* There is opportunity for all users to view the movie collection before signing up 	and signing in.
	* Movie cards with movie image reveals information about the movie with movie and 	book links.
	* There is a button to sign in and sign up in the menu.
	 * There is button to add favourite movies in the menu.
	* The website has Profile page with ability to edit user’s information and to edit and 	delete added movies.
	* There is search bar of movies by different categories and by the name on the 	movies page.
	* Movies page has movie filter by category.
	* Users can log out of the site securely.

	* User Admin has easy access to all areas of the website.
	* User Admin can manage any movie and manage movie categories.

* Ensure that all features work well: 
	* Each page has a responsive and fixed to the top navigation menu with active button to 	the current page link and with logo of website.
	*  Navigation menu has Home, Movies and SignIn/SignUp buttons for not signed up users 	and Profile, Add Movie, Log Out for signed up users. Additional button ”Manage categories” 	is for Admin user. There is a user’s name in the right corner of Menu.
	![img](https://github.com/Dynjashik/MSP3-Movie-collection/blob/master/static/images/README%20file/Menu.png)
	* Home Page is a main page and has a background image with a website title, welcome 	text and three 	recently added movies.
	![img](https://github.com/Dynjashik/MSP3-Movie-collection/blob/master/static/images/README%20file/Home_page.png)
	* Movies page has a list of all movie collection,  search box of movies by category, by title, 	movie filter by category. 
	![img](https://github.com/Dynjashik/MSP3-Movie-collection/blob/master/static/images/README%20file/Movies_page.png)
	* Movies cards has a user’s or default image with title, details button. Clicking on card 	movie information with book link opens with possibility to edit and delete them.
	![img](https://github.com/Dynjashik/MSP3-Movie-collection/blob/master/static/images/README%20file/Movie_card.png)
	* Clicking on SignIn/SignUp button SignIp form opens for signed up users. If user hasn’t 	signed up the page redirects to SignUp form. After signing in user is redirected to Home 	page.
	![img](https://github.com/Dynjashik/MSP3-Movie-collection/blob/master/static/images/README%20file/SignUp.png)
	* Profile page has signed in user’s information and user’s added movies with opportunity to 	update the information and manage movies(edit, delete).
	![img](https://github.com/Dynjashik/MSP3-Movie-collection/blob/master/static/images/README%20file/Profile.png)
	* Clicking on ”Add movie” button in Menu page opens with form with input fields: movie 	name, 	category name, year, 	duration description, movie and book link, optional movie 	image and submit button. 
	![img](https://github.com/Dynjashik/MSP3-Movie-collection/blob/master/static/images/README%20file/Add_movie.png)
	* On Movie page clicking on ”edit movie” button by creator, page opens with filled input 	fields with movie information and ”submit” and ”back” buttons to update it or not. Clicking on 	”back” button page redirects to movie page without any changes.
	* Admin user have access to manage categories and manage any movie on the website, 	clicking on ”Manage Categoties” button in Menu.
	![img](https://github.com/Dynjashik/MSP3-Movie-collection/blob/master/static/images/README%20file/manage%20categories.png)
	* After any actions on the website such as signing in and signing up, add, edit and delete movie, update personal information, log out and etc flash messages open in pop up windows with informativ text or confirming question.
	* There is double checking modals before deleting any information.
	![img](https://github.com/Dynjashik/MSP3-Movie-collection/blob/master/static/images/README%20file/modal.png)
	* The password field uses Werkzeug to hash the password on entry and double confirm 	password is validated using Javascript.

Mobile testing!
The following online validators have been used for checking the code for any errors or warnings:
* [W3C HTML Validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmy-milestone-project3.herokuapp.com%2Fhome);  
There are no warnings or errors.

* [W3C CSS Validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fmy-milestone-project3.herokuapp.com%2Fhome&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en);  
There are 1 error and warnings connected to external libraries (MaterializeCSS,Awesome, hover.css) that I cannot correct.

* [JShint](https://jshint.com/) looks good:  
![img]()

Lighthouse testing was made in Chrome browser developer tools. 
* Desktop Lighthouse Improved Report:  
![img]()

* Mobile Lighthouse Report:  
![img]()

The site was tested across different browsers and screen sized to be sure in responsiveness and browser compatibility.: Chrome, Internet Explorer, Safari, Firefox, UC Browser, Opera and Samsung Internet. It was also tested on mobile devices such as: iPhone Xs, iPhone 7, iPhone 11, Xiaomi Redmi Note 9. 

## Deployment

Steps for deploying the website to a hosting platform using Heroku:

1. Set up requirements.txt file by typing in the terminal; pip3 freeze –local > requirements.txt to tell Heroku which applications and dependencies are required to run our app.
2. Set up a Procfile file by typing: echo web: python app.py > Procfile. Access the Procfile and delete the bottom empty line.
3. Open Heroku.com and log in on a dashboard where select “Create a New App”. Create an App name “my-milestone-project3”, choose the closest region Europe and click “Create App”.
4. Head over to the “Deploy” tab and choose the “Deployment method” GitHub, adding the repository name MSP3-Movie-collection. Then click “search” and “Connect” to the repository name.
5. Go to the “Settings” tab, and scroll down to “Config Vars”. Click “Reveal config vars” and fill in the Key and Value pairs, copied from env.py file:
          * IP : 0.0.0.0
          * PORT : 5000
          * SECRET_KEY : YOUR_SECRET_KEY
          * MONGO_URI : “mongo db [link](mongodb+srv://DaBel:Be1User@cluster0.zi7ip.mongodb.net/myProject3?retryWrites=true&w=majority)”
          * MONGO_DBNAME : “database name(myProject3)”
6. Back within the terminal, add requirements.txt and Proclife files, do git commit and push them to GitHub.
7. Head back to the “Deploy” tab in Heroku, scroll down to “Automatic deploys”, click on “Enable Automatic Deploys” then “Deploy Branch”.
8. During a minute it should be message "Your app was successfully deployed." Click "View" to launch the new app.
Click on “Open App” which will launch the deployed app.

## Bugs

 

## Credits

### Contents

All content is written by developer Darya Belarusik.

### Media

Images for background, movie cards were taken from: [pngtree](https://pngtree.com/freebackground/private-cinema-advertising-background_911781.html) - private Cinema Advertising Background that provides images for commrecial use.
[LitHub](https://lithub.com/the-best-literary-adaptations-to-stream-over-thanksgiving-break-or-right-now/) -  for background image on home page.
Logo of the website at the navigation menu is created by Darya.

### Acknowledgements

[Movies by books](https://www.bookbub.com/blog/best-movies-based-on-books-all-time) – inspiration for list of movies based on books.

Inspiration for this project was received from:
* Other code institute students' projects.
* Help of the mentor, flask and my husband.