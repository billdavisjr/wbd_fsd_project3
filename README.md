#
# Full Stack Development Milestone Project #3

Student / Developer:
## Bill Davis
- bill.davis@gmail.com
- +1 (515) 999-0622

#
# Site name: "Quotations.Space!"

## WEB SITE ADDRESS:

- https://wbd-fsd-project3.herokuapp.com/

## GIT REPOSITORIES

- https://github.com/billdavisjr/wbd_fsd_project3.git

- https://git.heroku.com/wbd-fsd-project3.git

NOTE: The issues (bugs, features) I had compiled in my original repository on GitHub for this project are not part of a Git repo 
and so did not copy over when I cloned the repo for submission of this project to Code Institute.  

I cloned it before submitting it because I plan to keep working on the project outside the scope of the course and we're not 
supposed to change the repo after we submit it.  If you wish to see the issue database from the original repo, let me know by 
email and I will provide the URL.  I only mention this because some of the branches, done for working on bugs, are titled "issNN" 
(where NN is the number of the issue in the GitHub issues database.) This naming comes from the book provided on the Git web site 
and I found this method useful and have started using it to work on bugs and enhancements.

#
# PROJECT INTRODUCTION

## Reasoning for the project

For several decades now I have used a quotations database I created to learn how to program on a variety of systems, from OpenVMS DCL 
command line on VAX and Alpha minicomputers, to Visual Basic 6 and VB.NET / Visual Studio IDEs to create desktop apps on Windows, 
to Java desktop apps (.jar) on Windows and Mac (including a stand-alone desktop app on the Mac) and then on to JavaServer Pages using 
Eclipse.  This allows me to learn how to use the basic CRUD concepts on a particular platform.  Over the years I have collected 
thousands of quotes to use as well.  

So of course, I wanted to do the same thing when taking this course on modern full-stack web development from Code Institute. 

I realized quickly that the Task Manager mini-project that is developed as you go through the Data Centric Development module of the
 FSD course would be a perfect fit for my Quotations project, so I actually started developing it in parallel as the course went 
 through the mini-project, adapting and modifying it for my needs.  For example, I added a search feature and 
 some sorting of the databases (quotations sorted by person's name, categories sorted by category name) as well as data items such 
 as "favorite" (instead of urgent), source of the quote, star rating (1-5), and date said. 

I'll be continuing to develop (a copy of) this project after I have finished the Code Institute Course for personal use and perhaps 
as a side business/hobby.  I've actually purchased the domain name quotations.space and quotation.space (singular) for use with 
this site. 

#
# WHO IS THIS WEB SITE FOR? 

Right now this web site is for my personal/family use in collecting quotations that I enjoy. In the future I would like this site 
to be \available for the use of anyone in the world to locate, contribute and save their own quotes or quotes from a large 
database of existing quotes.  


## WHAT DO THEY WANT TO DO WHEN THEY VISIT
- Search for relevant quotes by category or keyword searches
- Maintain a database of quotes
- Sort and filter the list of quotes (eventually)
- Output the quote to email, text message, the clipboard, on a photo, on a t-shirt, etc. (eventually)

#
# USER STORIES

User stores are statements of the form "As a *user type*, I want to perform an *action*, so I can achieve a *goal*.

- As a collector of quotes, I want to store my quotes in a database, so I can access them anywhere.

- As a fan of quotes, I want to be able to search for a quote using a few words, so I can find it and use it.

- As a write, I need to be able to search for quotes by category or keyword, so I can start a chapter or section with an appropriate quote.

- As someone who is putting together a presentation, I need to be able to search for a relevant quote, so that I can put it in my presentation.

FUTURE: 

- As someone wanting a gift for a friend, I want to find or add a quote relevant to my friend, then have it put on a poster, t-shirt or coffee mug.


#
# DESIGN

## MOCKUPS / WIREFRAMES 

Mockups/wireframes of the design for the main page and the add and edit quotations pages are in the source code repository 
in the /design/mockups folder. 

The categories page and add/edit categories pages are the same as the quotes and add/edit quotes 
page, just simpler and missing the search field which was unnecessary.


## PAGE DESIGN

The site is designed to present the quotes in the form of "cards".  I wanted it to look like quotes you see hanging on a wall. 
There is an unobtrusive button at bottom left of the card (the popular 3-line "hamburger" icon) that lets you expand the card 
and show more information about the quote such as the category, source of the quote (if known), date the quote was said (if known),
star raging (0-5 with half-stars allowed) and "favorite" status.  This favorite status is also shown at bottom right of the 
unexpanded quote if the quote has been set as a favorite. 

Clicking the icon also reveals the edit (pencil) and delete (trash can) icons for that particular quote so you can edit or 
delete that quote; I do need to add a confirmation to that delete. I will be implementing that through Materialize Modals 
in some future version (not the one I submitted to Code Institute.)

A floating mobile menu button hovers in the bottom right corner of the page as it does in many modern mobile apps from Google and 
other sites. Clicking it expands a menu of functions you can select to add new quotes or categories, display the list of quotes 
or categories, etc.  This floating menu button is available on ALL pages. 

To add or edit the quotes or view a list of categories,  you're taken to a separate page with fields you can fill out. 

There is also an "About this site" button on the floating menu.

The desktop and mobile sites look the same and is intentionally as minimal as possible. I don't want the interface to distract 
from the quotes. 

Since the site is called "Quotations.Space!", I found a "Star Trek" like animated GIF of stars streaming past and used that behind 
the header. I have also registered quotations.space and quotations.space as domain names and will be pointing them at a future 
version of this site when it is ready for the public.

# SITE FEATURES

- You can search for quotes; the database is indexed on the quote text and person's name and the source of the quote.
- You can add new quotes to the database
- You can remove existing quotes from the database
- You can edit existing quotes
- You can add, edit and delete categories for the quotes
- Most features are accessible by the floating menu button from any page. 

#
# DEPLOYMENT

NOTE: This project started from the Code Institute student template for Gitpod which preinstalls most of the tools needed for basic 
development.  It does not seem to be required to stand up this site from the Git repo in GitPod or Heroku, though you do need to 
install a few Python frameworks with the pip3 command in GitPod. The site is configured to have Heroku install those dependencies 
through the requirements.txt file, automatically. 

*REQUIREMENTS*

- Python 3
- Git 
- A GitHub free (or paid) account
- A Heroku free account (or paid, some other hosting environment, if you want -- you're on your own there, though)
- MongoDB free (or paid) account

- Python Frameworks
    - Flask
    - PyMongo (flask-pymongo)
    - dnspython

- Materialize CSS Framework  (don't need to install this)
- jQuery JavaScript framework (don't need to install this)

As of this writing, the requirements.txt file lists the following Python frameworks and versions.
Some are additional frameworks used by the ones listed above:

- click==7.1.2
- dnspython==1.16.0
- Flask==1.1.2
- Flask-PyMongo==2.3.0
- itsdangerous==1.1.0
- pymongo==3.10.1
- Werkzeug==1.0.1

NOTE: These are not necessarily the latest versions of these frameworks. 

#
# SETUP PROCESS

- Create a free MongoDB Atlas account and set up a database

    - ∂https://www.mongodb.com/cloud/atlas/signup

Set a database and the following collections:

    DATABASE STRUCTURE

        Database: quotations_space
        
            Collections:

                quotations
                    _id (autogenerated)
                    category_name               String
                    quotation_text              String
                    person                      String
                    source                      String 
                    date_said                   String
                    stars_rating                String
                    is_favorite                 String

                categories
                    _id  (autogenerated)
                    category_name               String

- Set up a text search so you can search multiple fields for a keyword with one search command. This is used by the search 
field on the quotes.html page.   See https://docs.mongodb.com/manual/core/index-text/

    -  This project is set up a text index on quotation_text, person, and source fields.  
        - Category_name might be another good field to add to the index

    - The running site provided:

        - http://wbd-fsd-project3.herokuapp.com/search_quotes

    is set up using a database with that text index described above for the search field. 

   You can also set up a text index to just search ALL text (string) fields in the collection; see the web page linked above.

- Add a few quotes in manually to these collections and give the quotes a category from the categories collection. 

- If you want to use the MondoDB test database I used to develop and test this site, contact me and I'll send you the connection string. 

- Set up a GitPod free account

    - If you want to use some other environment, feel free, of course, but these instructions assume GitPod and GitHub and Heroku.

- Set up the needed environment variables in GitPod or your IDE
    
    - See https://www.gitpod.io/docs/environment-variables/ for info on how to do that

    - IP = 0.0.0.0
    - PORT = 5001
    - QS_MONGO_URI =  (the address for your Mongo database created earlier

- Use the Chrome web browser with GitPod. Install the GitPod GitHub button Extensions so you can create a new GitPod workspace
from your clone of my repo. 

    https://chrome.google.com/webstore/detail/gitpod-dev-environments-i/dodmmooeoklaejobgleioelladacbeki

- Set up a Heroku account.  

    - If you want to use some other web app hosting environment or host it locally you may, but these instructions assume hosting on Heroku. 

- Create a Heroku project you'll clone my repo into.

- Clone or copy the Quotations.Space! project into your GitPod project.  

    - https://github.com/billdavisjr/wbd_fsd_project3.git

    - https://git.heroku.com/wbd-fsd-project3.git


- install the following frameworks from the GitPod command line:

    - $ pip3 install flask
    - $ pip3 install flask-pymongo
    - $ pip3 install dnspython

- Create the Heroku Requirements pip3 freeze > requirements.txt file if needed at the root directory of the project (should 
already be present in the repo, but this is how to update it if you have any problems deploying the site to Heroku)

    - $ pip3 freeze > requirements.txt

- Create the Heroku Procfile if needed at the root directory of the project on GitPod (should not be needed)

    - $ echo web: python app.py >Procfile

- Set up same environment variables in Heroku (or your own environment if not) if you using Heroku for hosting

    - IP=0.0.0.0. (may be provided by web/app server)
    - PORT=5001   (may be provided by web/app server)
    - QS_MONGO_URI  

https://devcenter.heroku.com/articles/config-vars

- Heroku setup in GitPod

    - $ heroku login
    - $ heroku ps:scale web=1       (this may not be needed)

- Link the Heroku Git repo to your GitPod workspace so you can push 

    - $ heroku git:remote -a YOUR_HEROKU_PROJECT NAME

- Build the Heroku app (must be logged in to heroku)

    - % git push heroku master        

These IP addresses are set up in the Heroku web app for a particular app under Settings in the "Config Vars" section.
I think the system provides / set the IP and PORT variables anyway. 

#
# Starting up the Project 

## STARTING LOCALLY (in GitPod)
To run a local copy of the site on GitPod, type:

- $ python3 app.py

- A blue button should appear to click: *Make Public*,
- Another blue button should appear to click: *Open Browser* (or Open Preview if you want to use the preview window in GitPod)

- NOTE: In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in 
the bash terminal.

To STOP the web server running the site, press Ctrl+C in the window where you ran `$python3 app.py` 
command and the server will stop and return you to the command prompt.


## STARTING ON HEROKU

Once the app has been deployed to Heroku you can use Heroku itself to start/stop the app.

You can also start (or restart/deploy the app after changing the code) by associating the Heroku
git repository with the local git repo as a remote:

   - $ heroku git:remote -a <heroku_project_name>

Then after changing some code do a:

-  $ git push        (to push to origin master, e.g. GitHub)

and a 

   - $ git push heroku master   
   
to push to the heroku remote Git repo too. This also rebuilds and redeploys the app on Heroku.

#
# TESTING

## TEST PLAN

### Testing environments

### EQUIPMENT:
- Mac OS X (MacBook Pro and iMac)
- iPhone smartphone ()
- iPad tablet

NOTE: I do not have access to Android or Windows or Linux equipment to test on at this time.  
I cannot test on Windows at work because Heroku is blocked and we are not allowed
to install software on our machines. 

### TESTS

`NOTE: Problems should be logged in in the Issues tab on the GitHub repo.`. (they were when I was created this site, 
but are not part of the Git repo and so were not transferred when I cloned this site to a new repo for submission to 
CodeInstitute.)

- Test that the site and all pages look and functions well on all platforms and. browsers
    - On desktop PC, test using different window widths and heights, especially largest and smallest widths and heights.
    - On smartphones and tablets, test in both portrait and landscape orientation.

PLATFORMS & BROWSERS:
    - iPhone:   Safari, Chrome, Firefox, Edge, Opera
    - iPad:     Safari, Chrome, Firefox, Edge, Opera
    - Mac:      Safari, Chrome, Firefox

- Add new quotes, test all the fields, and field validations
    - Add stars with values from 0 to 5 as well as fractions such as 
        - 0, 0.5, 1.5 ... 4.5, 5.0
        - Also try other fractions besides .5
        - Also try integers other than 0,1,2,3,4,5 

    - Most of the database fields are plain text so little validation is needed, and leaving them blank is ok in most cases, though
    you are unlikely to do so except perhaps for the Date Said and Source of the quote; you often won't know either. 

- Have at least one other person try the site, and get feedback/bug REPOSITORIES
    - Had my wife do so and got good feedback on several problems and GUI suggestions, all fixed. 


### CODE VALIDATION

The GitPod IDE has linters/validators for HTML, CSS, JavaScript, Python etc.  I installed one for Jinja from the Extensions 
icon in the lefthand sidebar in GitPod.

Because this code uses Flask and Jinja templates, many of the HTML templates are fragments of HTML and so don't entirely 
validate (usually it's only just the first line) and have tagged {% %} code lines.  For those you simply have to keep an eye on the 
"Problems" tab in the GitPod IDE and see if anything shows up beyond a few errors you'll always get on the template HTML files, 
which are:

- Doctype must be declared first   
    - (you'll get this on all the templates; the templates don't start with HTML tags because those are only in the base.html template)

- The id value [is_favorite] must be unique 
    - (or similar - this is an example of HTML surrounded by {% if %} block so. that we can display a checkbox as checked or not)

The GitPod IDE will mark files with code validation problems with a tiny badge on the document icon in the file explorer and also
in the tab at the top of the editor when the file is being edited.

Also keep an eye on the last tag in the template HTML files as it will often be flagged as a problem if you have unbalanced 
open/close tags somewhere.

The validator for Python flags long lines, as well, and this is a good indication to clarify long, complicated lines into several 
simpler, cleaner, clearer lines. The example mini-project "Task Manager" frankly had a number of those.  Indenting helped makes 
them clearer, but refactoring into separate lines with a single clear purpose also made for better, less complicated code.

#
# FUTURE PLANS

I have many future plans for this project. 
Note that I have cloned a copy of the GitHub repo I submitted for grading, and am continuing development on that copy.

Ideas include:

- Adding a "sort by" control by the search field

- Adding a "filter by" control by the search field  Allow sorting or filtering by name, favorites status, stars rating, category, etc.

- Add a confirmation dialog before deleting a record. 

- Add a quote of the day based on:
    - people's birthday in the database
    - or on the date-said data in the database

- Allow setting favorite status by just clicking the favorites icon on the quote; 
    - solid hear icon = favorite, outlined heart icon = not favorite

- Display the stars icons next to the favorites icon (or perhaps one on the left side and one on the right side)
and allow the user to set the number of stars by clicking. Allow half-stars, too, possibly

- Add additional control beyond edit and delete, such as:
    - share (to email or text the quote)
    - meme (to let you put the quote on a nice photo from a free stock photo site such as Pexels, or an uploaded photo)

- Allow pagination of the database so that thousands of quotes are allowed

- Also have much more condensed, tabular/spreadsheet style view of the data

- Allow import and export of data in CSV or XML format. 

- Allow setting up a user account so people can have their own quotes database or add quotes from our database to theirs. 

- Additional database items:

    - A separate `persons` table with additional fields
        - vocation
        - first name
        - middle initial
        - middle name
        - last name
        - vocation
        - birthday (mm/dd/yyyy)
        - born (yyyy)
        - died (yyyy)
        - notes

        I also want to add some links to a photo and bio information for the people:
        - wikimedia-photo-url
        - wikimedia-attribution-url
        - wikipedia-bio-url
    
        This data will be accessed using the 'persons' field in the quotations collection the same way we do 'categories' now.
        It can be useful for sorting, displaying quotes on someone's birthday, searching, etc. 

    - Additional fields for the `quotations` collection:
        - language
        - link to Amazon to purchase to the book the quote is from (Associates program)
        - link to one of the many sites to get the quote printed on a T-Short, poster, mug, whatever.
        - notes
        
#
# ATTRIBUTIONS / CREDITS / ACKNOWLEDGEMENTS

- This project started from the Code Institute student template for Gitpod which preinstalls most of the tools needed for 
basic development.

    - https://github.com/Code-Institute-Org/gitpod-full-template

- It also was adapted from the Task Manager mini-project created in the course, modified heavily to change the GUI and add 
additional functions such as searching. 

    - https://github.com/Code-Institute-Solutions/TaskManager/

- The CSS framework used for the site is MaterializeCSS
    - https://materializecss.com/
    - http://archives.materializecss.com/0.100.2/about.html

- Third-party Python frameworks used are:
    - Flask                 https://palletsprojects.com/p/flask/
    - flask-pymongo         https://pypi.org/project/pymongo/ 
    - dnspython

and the frameworks they in turn might use; see the requirements.txt file (or view it with `$pip3 freeze` command.)

- Third party JavaScript frameworks
    - jQuery      https://jquery.com/

- Development Tools
    - GitPod integrated development environment     https://www.gitpod.io/
    - GitHub code repository                        https://www.github.com/
    - Heroku web app hosting                        https://www.heroku.com/
    - Python language                               https://www.python.org/
    - Mongo Database                                https://www.mongodb.com/
     
 - The animated starfield behind the page header is from WikiMedia Commons
    - https://commons.wikimedia.org/wiki/File:StarfieldSimulation.gif
    - https://upload.wikimedia.org/wikipedia/commons/e/e4/StarfieldSimulation.gif

