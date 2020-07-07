#
# Full Stack Development Milestone Project #3

Student / Developer:
## Bill Davis
- bill.davis@gmail.com
- +1 (515) 999-0622

#
# Site name: "Quotations.Space!"

## WEB SITE ADDRESS:

    << CLONE THE EXISTING ONES AND THE EXISTING HEROKU APP BEFORE SUBMITTING>>
    Name in the style of FSD1 and FSD2

## GIT REPOSITORIES


<< CLONE THE EXISTING ONES AND THE EXISTING HEROKU APP BEFORE SUBMITTING>>

<< ALSO USE THIS TO TEST THE DEPLOY INSTRUCTIONS>>

#
# PROJECT INTRODUCTION & DESIGN

## Reasoning for the project

For several decades now I have used a "quotations" database to learn how to program on a variety of systems, from OpenVMS DCL 
command line on VAX and Alpha minicomputers, to Visual Basic 6 and VB.NET / Visual Studio IDEs to create desktop apps on Windows, 
to Java desktop apps (.jar) on Windows and Mac (including a stand-alone desktop app on the Mac) and then on to JavaServer Pages using 
Eclipse.  This allows me to learn how to use the basic CRUD concepts on a particular platform.  Over the years I have collected
 thousands of quotes to use as well.  

So of course, I wanted to do the same thing when taking this course on modern full-stack web development from Code Institute. 

I realized quickly that the Task Manager miniproject that is developed as you go through the Data Centric Development module of the
 FSD course would be a perfect fit for my Quotations project, so I actually started developing it in parallel as the course went 
 through the mini-project, though I also started adapting and modifying it for my needs.  For example, I added a search feature and 
 some sorting of the databases (quotations sorted by person's name, categories sorted by category name) as well as data itemus such 
 as "favorite" (instead of urgent), source of the quote, star rating (1-5), date said, a link to a photo from Wikimedia Commons, 
 etc. 

I wanted both a "favorites" and a "star rating" system for quotes, and the ability to share quotes via email (possibly other means 
such as texting, copy-and-paste, etc later) and to "meme" the quote onto an image background. I was not able to implement all of 
those features as time allows, but I will in the future as a platform to practice and expand what I am learning. I may actually 
make the site look more like Google at some point - start out with just a search field. That's what I did when I developed a web 
app using Java Server Pages, for example. I have registered the domain name "quooqle" (Q's not G's) but am not sure if I want to 
use it. Google has more money for lawyers than I do!  So I also reqistered quotation.space and quotations.space long before I 
started this project (the later is the plural of the former.).  I plan to hook those up to this site eventually. 

I'll be continuing to develop this project after I have finished the Code Institute Course for personal use and perhaps as a side 
business.  

---

# WHO IS THIS WEB SITE FOR? 

Right now this web site is for my personal use in collecting quotations that I enjoy. In the future I would like this site to be 
available for the use of anyone in the world to locate, contribute and save their own quotes or quotes from a large database of 
existing quotes.  


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

- As a write, I need to be able to search for quotes by category or keyword, so I can start a chapter or section with an appopriate quote.

- As someone who is putting together a presentation, I need to be able to search for a relevant quote, so that I can put it in my presentation.

- As someone wanting a gift for a friend, I want to find or add a quote relevant to my friend, then have it put on a poster, t-shirt or coffee mug.


#
# DESIGN

## MOCKUPS / WIREFRAMES 

Mockups/wireframes of the design for the main page and the add and edit quotations pages are in the source code repository 
in the /design/mockups folder. 

The categories page and add/edit categories pages are the same as the quotes and add/edit quotes 
page, just simpler and missing the search field which was unnecessary.


## PAGE DESIGN

The site is designed to present the quotes in the form of "cards", with an unobtrusive button that lets them expand the card and
show more information about the quote.  I wanted it to look like quotes you see hanging on a wall. 

To add or edit the quotes or categoies you're taken to a separate page with fields you can fill out. 

The desktop and mobile sites look the same; I don't want the interface to distract from the quotes.  A floating mobile menu button 
hovers in the bottom right corner as it does in many modern mobile apps from Google and other vendors. Clicking it expands a menu 
of functions you can select to add new quotes or categories, display the list of quotes or categories, etc.  This floating menu 
button is available on ALL pages. 

Since the site is called "Quotations.Space!", I found a "Star Trek" like animated GIF of stars streaming past and used that behind 
the header. I have also registered quotations.space and quotations.space as domain names and will be pointing them at a future 
version of this site when it is ready for the public.

# SITE FEATURES

- You can search for quotes; the database is indexed on the quote text and person's name
- You can add new quotes to the database
- You can remove existing quotes from the databaes
- You can edit existing quotes
- You can add and delete new categories for the quotes
- Most features are accessible by the floating menu button from any page. 

#
# DEPLOYMENT

NOTE: This project started from the Code Institute student template for Gitpod which preinstalls most of the tools needed for basic 
development

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

- Materialize CSS Framework 
- jQuery JavaScript framework

As of this writing, the requirements.txt file lists the following Python frameworks and versions.
Some are additional rameworks used by the ones listed above:

- click==7.1.2
- dnspython==1.16.0
- Flask==1.1.2
- Flask-PyMongo==2.3.0
- itsdangerous==1.1.0
- pymongo==3.10.1
- Werkzeug==1.0.1

NOTE: These are not necesssarily the latest versions of these frameworks. 

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
                    wikicommons_photo           String
                    wikicommons_attribution     String
                    wikipedia_bio               String

                categories
                    category_name               String

                In future I will create a "persons" collection and move the 
                    wiki& fields to that, and look up information from it
                    using the "person" name, as we do for categories. 

 - Add a few quotes in manually to thease collectons and give the quotes a category from the categories collection. 

- If you want to use the MondoDB test database I used to develop and test this site, contact me and I'll send you the connection string. 

- Set up a GitPod free account

    - If you want to use some other environment, feel free, of course, but these instructions assume GitPod and GitHub and Heroku.

- Set up a Heroku account.  

    - If you want to use some other web app hosting environment or host it locally you may, but these instructions assume hosting on Heroku. 

- Clone or copy the Quotations.Space! project into your GitPod project. 

    - << add GitHub URL for final submitted project here> - << clone this to a FSB_Milestone_Project_3 repo and replace this URL 
    BEFORE submitting this project. >>

- install the following frameworks from the GitPod command line:

    - $ pip3 install flask
    - $ pip3 install flask-pymongo
    - $ pip3 install dnspython

- Create the Heroku Requirements pip3 freeze > requirements.txt file if needed at the root directory of the project:

    - $ pip3 freeze > requirements.txt

- Create the Heroku Procfile if needed at the root directory of the project

    - $ echo web: python app.py >Procfile

- Other Heroku setup (if you're using it)

    - $ heroku login
    - $ heroku ps:scale web=1

- Set up the needed environment variables in GitPod or your IDE
    
    - See https://www.gitpod.io/docs/environment-variables/ for info on how to do that

    - IP = 0.0.0.0
    - PORT = 5001
    - QS_MONGO_URI =  (the address for your Mongo database screated earlier

- Set up same environment variables in Heroku (or your own environment if not) if you using Heroku for hosting
    - IP=0.0.0.0. (may be provided by web/app server)
    - PORT=5001   (may be provided by web/app server)
    - QS_MONGO_URI   

These IP addresess are set up in the Heroku web app for a particular app under Settings in the "Config Vars" section.
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

You can also start (or restart/reploy the app after changing the code) by associating  the Heroku
git repository with the local git repo as a remote:

    - $ heroku git:remote -a <repository>

<< make sure this is all you need to do >>

Then after changing some code do a:

    -  $ git push        (to push to origin master, e.g. GitHub)

and a 

    - $ git push heroku master   (to puth to the heroku remote Git repo too. This also 
                                  rebuilds and redeploys the app on Heroku) 

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

`NOTE: Problems should be logged in in the Issues tab on the GitHub repo.`

- Test that the site and all pages looks and functions well on all platforms.
    - On desktop PC, test using different window widths and heights
    - On smartphones and tablets, test in both portrait and landscape orientation.

PLATFORMS:
    - iPhone:   Safari, Chrome, Firefox, Edge, Opera
    - iPad:     Safari, Chrome, Firefox, Edge, Opera
    - Mac:      Safari, Chrome, Firefox

- Add new quotes, test all the fields, and field validations
    - Add stars with values from 0 to 5 as well as fractions such as 
        - 0.5, 1.5 ... 4.5, 5.0
        - Also try other franctions besides .5
        - Also try integers other than 0,1,2,3,4,5 

    - Most of the database fields are plain text so little validation is needed, and leaving them blank is ok in most cases, though
    you are unlikely to do so except perhaps for the Date Said and Source of the quote; you often won't know either. 


### CODE VALIDATION

The GitPod IDE has linters/validators for HTML, CSS, JavaScript, Python etc.  I installed one for Jinja from the Extensions 
icon in the lefthand sidebar in GitPod.

Because this code uses Flask and Jinja templates, though, many of the HTML templates are fragments of HTML and so don't entirely 
validate (usually it's only just the first line) and have tagged {% %} code lines.  For those you simply have to keep an eye on the 
"Problems" tab in the GitPod IDE and see if anything shows up beyond a few errors you'll always get on the template HTML files, 
which are:

- Doctype must be declared first   
    - (the templates don't start with HTML tags because those are only in the base.html template)

- The id value [is_favorite] must be unique 
    - (or similar - this is an example of HTML surrounded by {% if %} block so. that we can display a checkbox as checked or not)

The GitPod IDE will mark files with code validation problems with a tiny badge on the document icon in the file explorer and also
in the tab at the top of the editor when the file is being edited.

Also keep an eye on the last tag in tje template HTML files as it will often be flagged as a problem if you have unbalanced 
open/close tags somewhere.

The validator for Python flags long lines, as well, and this is a good way to clarify long, complicated lines into several simpler, 
cleaner, clearer lines. The example miniproject "Task Manager" frankly had a number of those.  Indenting helped make they clearer, 
but refactoring into separate lines with a single clear purpose also made for better code.


#
# FUTURE PLANS

I have many future plans for this project.  Some of them are in the GitHub repo's Issues section as "enhancement requests".  
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

- Add addional control beyond edit and delete, such as:
    - share (to email or text the quote)
    - meme (to let you put the quote on a nice photo from a free stock photo site such as Pexels, or an uploaded photo)

- Allow pagination of the database so that thousands of quotes are allowed

- Also have much more condensed, tabular/spreadsheet style view of the data

- Allow impoprt and export of data in CSV or XML format. 

- Allow setting up a user account so people can have their own quotes database or add quotes from our database to theirs. 

- Additional databaes items:

    - A separate `persons` table with addtional fields
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
        - wikepedia-bio-urk
    
        This data will be accessed using the 'persons' field in the quotations collection the same way we do 'categories' now.
        It can be useful for sorting, displaying quotes on someone's birthday, searching, etc. 

    - Additonal fields for the `quoatations` collection:
        - language
        - link to Amazon to purchase to the book the quote is from (Associates program)
        - link to one of the many sites to get the quote printed on a T-Short, poster, mug, whatever.
        - notes
        
#
# ATTRIBUTIONS / CREDITS / ACKNOWLEDGEMENTS

- This project started from the Code Institute student template for Gitpod which preinstalls most of the tools needed for basic development.

- It also was adapted from the Task Manager mini-project created in the course, modified heavily to change the GUI and add additional functions such as searching. 
 
- The CSS framework used for the site is MaterializeCSS
    - https://materializecss.com/
    - http://archives.materializecss.com/0.100.2/about.html

- Third party Python frameworks used are:
    - Flask                 https://palletsprojects.com/p/flask/
    - flask-pymongo         https://pypi.org/project/pymongo/ 
    - dnspython
    And the frameworks they in turn might use; see the requirements.txt file (or generate it)

- Third party JavaScript frameworks
    - jQuery      https://jquery.com/

- Development Tools
    - GitPod integrated development environment     https://www.gitpod.io/
    - GitHub code repository                        https://www.github.com/
    - Python language                               https://www.python.org/
    - Mongo Database                                https://www.mongodb.com/
     
 - The animated starfield behind the page header is from WikiMedia Commons
    - https://commons.wikimedia.org/wiki/File:StarfieldSimulation.gif
    - https://upload.wikimedia.org/wikipedia/commons/e/e4/StarfieldSimulation.gif

