![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome Dynjashik,

This is the Code Institute student template for Gitpod. We have preinstalled all of the tools you need to get started. You can safely delete this README.md file, or change it for your own project. Please do read it at least once, though! It contains some important information about Gitpod and the extensions we use.

## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

## Updates Since The Instructional Video

We continually tweak and adjust this template to help give you the best experience. Here is the version history:

**October 21 2020:** Versions of the HTMLHint, Prettier, Bootstrap4 CDN and Auto Close extensions updated. The Python extension needs to stay the same version for now.

**October 08 2020:** Additional large Gitpod files (`core.mongo*` and `core.python*`) are now hidden in the Explorer, and have been added to the `.gitignore` by default.

**September 22 2020:** Gitpod occasionally creates large `core.Microsoft` files. These are now hidden in the Explorer. A `.gitignore` file has been created to make sure these files will not be committed, along with other common files.

**April 16 2020:** The template now automatically installs MySQL instead of relying on the Gitpod MySQL image. The message about a Python linter not being installed has been dealt with, and the set-up files are now hidden in the Gitpod file explorer.

**April 13 2020:** Added the _Prettier_ code beautifier extension instead of the code formatter built-in to Gitpod.

**February 2020:** The initialisation files now _do not_ auto-delete. They will remain in your project. You can safely ignore them. They just make sure that your workspace is configured correctly each time you open it. It will also prevent the Gitpod configuration popup from appearing.

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the <a href="https://github.com/Eventyret/vscode-bcdn" target="_blank">README.md file at the official repo</a> for more options.

---

Happy coding!


# MS3 Movies collection

Movies collection is a website with a list of movies based on books where people can find movies by books of different genres that gives the opportunity to compare movie and book story. Movies have a link to watch them or link to buy a book for reading. Users also can recommend their favourite movies and books.

![]()

Live Website: []()

## Table of Contents
**[User Experience](#UX)** 

**[Features](#Features)**

**[Technologies](#Technologies)**

**[Testing](#Testing)**

**[Deployment](#Deployment)**

**[Bugs](#Bugs)**

**[Credits](#Credits)**

## UX

This project is created for people who like to watch quality movies with deep sense because stories based on books are always good and deep. It’s also interesting for booklovers to look at a book story with a different look and compare it with movie adaptation.

### User Stories

As a user I want to:
* Enjoy the design and navigate through the website easily.
* Have an opportunity to view/preview the website before registering an account.
* Have clear Sign In/Sign Up pages and 
* Have an ability and motivation to add their own recommendations.
* Have a possibility to edit and delete movies posted.
* Search the collection to find movies by different genres.
* Find short movie descriptions and links where they can watch movies and purchase the books.
* Have an ability to choose among several difficulty levels.
* Securely log out of the site.

As Admin I want to:
* Give easy entrance to all areas of the site.
* Have an ability to add, delete any movie, user.
* Be able to add and delete movie genres(categories).
* Have access to add affiliate links to each review left by a user, and earn money from those links
.

### Strategy

The goal is to create a good quality list of movies for quickly find a suitable movie or book for everybody and to advertise books. 

  

### Scope

Features that should be in the project:
* Main menu
* Home page with several recently added movie examples
* Movie page with movie collection with their description
* Several movie genres
* Search box for movies
* Add movie page for users signed up/in
* Edit and delete movie function
* Add movie genre(category) for Admin
* Log out

### Structure


### Skeleton

Mockup of the website was created in ["Balsamiq Wireframes"]().

### Surface


## Features


### Features left to implement

## Technologies

### Database

Mongo DB

### Languages used:

HTML5 - for basic content and structure of the site.  
CSS3 - for design.  
Javascript - logic for the game.
Python -   for writing the scripts to render all the different templates using flask. And connecting to mongodb

### Frameworks and libraries used:

Flask - a python web framework
PyMongo - python tool for use with Mongo DB.
Werkzeug - WSGI web application library used by Flask and Python.

[MaterializeCSS](https://materializecss.com/) (navbar, buttons, badge, modal) - provides styling, layout and responsiveness of the website.  
[JQuery](https://jquery.com/) - for making the site interactive.  
[Font Awesome](https://fontawesome.com/) - for using icons.  
[Balsamiq](https://balsamiq.com/) - for creating a mockup.  
[Dog API](https://dog.ceo/dog-api/about) - for dog pictures.  


### Tools and Other Resources used:

[Github](https://github.com/) -  for version control and pushing content to repository.  
[Gitpod](https://www.gitpod.io/)  -  for building the site. 
[Heroku](https://id.heroku.com/login) - for deploying the project
[TinyPNG](https://tinypng.com/) - for reducing the size of images.  
[Wfonts](https://www.wfonts.com/font/comic-sans-ms) - for font of the website.  
[COLOR TOOL](https://material.io/resources/color/) - for color palettes and the accessibility of any color combination for UI.  
[Mockup generator](http://techsini.com/multi-mockup/index.php) - for testing responsive website on various devices.  
[W3 Schools](https://www.w3schools.com/) - for HTML, CSS, JS tips.  
[Stackoverflow](stackoverflow.com) - for finding answers on questions.  
[Webformatter](https://webformatter.com/html) - for beautifying HTML, CSS, Javascript codes.

### Codes used:

Some of the code for the game was taken from the sources:
*  [Stackoverflow](https://stackoverflow.com/questions/2450954/how-to-randomize-shuffle-a-javascript-array) - for shuffling game cards.

## Testing

The following steps were taken to ensure the website works as intended:
* Ensure that all user stories are achieved:
   
  
 * Ensure that all features work well: 

The following online validators have been used for checking the code for any errors or warnings:
* [W3C HTML Validator]();  
There are no warnings or errors.

* [W3C CSS Validator]();  


* JShint looks good:  
![img]()

Lighthouse testing was made in Chrome browser developer tools. 
* Desktop Lighthouse Improved Report:  
![img]()

* Mobile Lighthouse Report:  
![img]() 


## Deployment

Steps for deploying the website to a hosting platform GitHub Pages:



## Bugs


    * Game area with number of cards depending on difficulty level where the user can play. Cards are real photos of dogs loaded randomly using dog.ceo API.
      Game area also displays time spent and number of card flips.
    * Button Restart allows the user to return to the modal popup with difficulty options.
    * Button Quit allows the user to return to Home Page.
    * Final modal popup shows results of the game. It opens when game is finished with Play Again button that acts identically as Restart.
    

## Credits

### Contents

All content is written by developer Darya Belarusik.

### Media


## Credits

### Contents

All content is written by developer Darya Belarusik.

### Media



### Acknowledgements

Inspiration for this project was received from:
* Other code institute students' projects.
* Help of the mentor and my husband.

