import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'quotations_space'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb+srv://root:r00tUser@cluster0-oxfue.mongodb.net/quotations_space?retryWrites=true&w=majority')

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_quotes')
def get_tasks():
    return render_template("quotes.html", 
            quotations=mongo.db.quotations.find())


@app.route('/add_quote')
def add_quote():
    return render_template('addquote.html',
        categories=mongo.db.categories.find() )


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
