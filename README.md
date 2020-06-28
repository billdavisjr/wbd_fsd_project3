# Full Stack Development Milestone Project #3

"Quotations.Space!"

https://quotations-space.herokuapp.com/


## Bill Davis
### bill.davis@gmail.com
### +1 (515) 999-0622


## Reasoning for the project

For several decades now I have used a "famous quotes" database to learn how to program on a variety of systems, from OpenVMS DCL command line on VAX and Alpha minicomputers, to Visual Basic 6 and VB.Net/Visual Studio IDEs to create desktop apps on Windows, to Java desktop apps (jar) on Windows and Mac (including a stand-alone desktop app on the Mac) and then on to JavaServer Pages using Eclipse.  This allows me to learn how to use the basic CRUD concepts on a particular platform.  Over the years I have collected thousands of quotes to use as well.  

So of course, I wanted to do the same thing when taking this course on modern full-stack development. 

I realized quickly that the Task Manager miniproject that is developed as you go through the Data Centric Development would be a perfect fit for my Quotations project, so I actually started developing it in parallel as the course went through the mini-project, though I also started adapting and modifying it for my needs.  For example, I added a search feature. I I want both a "favorites" and a "star rating" system for quotes, and the ability to share quotes via email (possibly other means such as texting, copy-and-paste, etc later) and to "meme" the quote onto an image background. I may not implement all of those features as time allows, but they are all ideas I have for this project both now and in the future.  I may actually make the site look more like Google at some point - start out with just a search field. That's what I did when I developed a web app using Java Server Pages, for example.  I actually registered the domain name "quooqle" (Q's not G's) but am not sure if I want to use it. Google has more money for lawyers than I do!  So I also reqistered quotation.space and quotations.space (the later is the plural of the former.)

I'll be continuing to develop this project after I have finished the Code Institute Course for personal use and perhaps as a side business. I have already reqistered the domain names quotation.space, quotations.space, and quooqle.com and will use them to make this web app publicly avaialble at some point. I just have not decided what domain to ultimately use. 


# Getting set up

## REQUIREMENTS
- Python 3
- Git 
- Heroku
- MongoDB
- Python
- Frameworks
    - Flask
    - PyMongo (flask-pymongo)
    - dnspython
    - (and the frameworks the in turn may just, such as Jinja)

    As of this writing, the requirements.txt file lists the following frameworks:

    - click==7.1.2
    - dnspython==1.16.0
    - Flask==1.1.2
    - Flask-PyMongo==2.3.0
    - itsdangerous==1.1.0
    - pymongo==3.10.1
    - Werkzeug==1.0.1

    NOTE: These are not necesssarily the latest versions of these frameworks. 

## SETUP 
- Set up a GitPod account. If you want to use some other environment, feel free, of course. 

- This project started from a clone of the Code Institute student template for Gitpod which preinstalls most of the tools needed for basic development.  

- Clone or copy the Quotations.Space! project into your project. 

    - https://github.com/billdavisjr/quotations-space 

    << clone this to a FSB_Milestone_Project_3 repo and replace this URL 
    BEFORE submitting this project. >>

- install the following frameworks:
    pip3 install flask
    pip3 install flask-pymongo
    pip3 install dnspython

- Create the Heroku Requirements pip3 freeze > requirements.txt file if needed at the root directory of the project:

    - $ pip3 freeze > requirements.txt

- Create the Heroku Procfile if needed at the root directory of the project

    - $ echo web: python app.py >Procfile

- Set up the environment variables in GitHub 
    https://www.gitpod.io/docs/environment-variables/

- Set up environment variables in Heroku (or your own environment if not)
    - IP=0.0.0.0. (may be provided by web/app server)
    - PORT=5001   (may be provided by web/app server)
    - MONGO_URI   

    MONGO_URI is the connection string to your database; get that from MongoDB.

    These IP addresess are set up in the Heroku web app for a particular app under Settings in the "Config Vars" section.
s
- Create the database in MongoDB (Atlas)

    - Database name: 'quotations_space'
        - Tables / Documents:
            - quotations
                - _id  (autoamtically created by MongoDB)
                - quotation_text (string)
                - person (string)
                - source (string)
                - category_name (string)
                - date_said (string)
                - is_favorite
                - stars_rating

            - categories
                - _id
                - category_name (string)

Enter a few of your favorite quotes. 

## Starting up the Project 

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: *Make Public*,

Another blue button should appear to click: *Open Browser*.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the backend lessons.

## ATTRIBUTIONS:

- This project started from the Code Institute student template for Gitpod which preinstalls most of the tools needed for basic development.

- It also was adapted from the Task Manager mini-project created in the course, modified to change the GUI and add additional functions such as searching. 

- The animated starfield behind the page header is from WikiMedia:
    - https://commons.wikimedia.org/wiki/File:StarfieldSimulation.gif
    - https://upload.wikimedia.org/wikipedia/commons/e/e4/StarfieldSimulation.gif

- The GUI framework used for the site is the Materialize framework
    - http://archives.materializecss.com/0.100.2/about.html

- Third party Python frameworks used are:
    - Flask
    - flask-pymongo
    - dnspython
    And the frameworks they in turn might use; see the requirements.txt file (or generate it)

- Third party JavaScript frameworks
    - jQuery

- Other 
    - Google Fonts / Material Icons
