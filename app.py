import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 
 
app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'tasks_manager'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb+srv://root:r00tUser@cluster0-oxfue.mongodb.net/tasks_manager?retryWrites=true&w=majority')
 
mongo = PyMongo(app)
 
 
@app.route('/')
@app.route('/get_quotes)
def get_tasks():
    return render_template("quotations.html", tasks=mongo.db.quotations.find())
 
 
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
