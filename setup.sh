# commands to set up the workspace 
pip3 install flask
pip3 install flask-pymongo
pip3 install dnspython

# add other installers here


pip3 freeze > requirements.txt

heroku git:remote quotations-space

