# Commands to set up the workspace 

# INSTALL PYTHON PACAKAGES & CREATE REQUIREMENTS FILE

pip3 install flask
pip3 install flask-pymongo
pip3 install dnspython
# add other installers here
pip3 freeze > requirements.txt

# HEROKU SETUP

heroku git:remote quotations-space
heroku domains:add 'quotations-space'
