import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'quotations_space'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb+srv://root:r00tUser@cluster0-oxfue.mongodb.net/quotations_space?retryWrites=true&w=majority')

# 'mongodb+srv://root:r00tUser@cluster0-oxfue.mongodb.net/quotations_space?retryWrites=true&w=majority'
# 'mongodb://localhost'

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_quotes')
def get_quotes():
    return render_template('quotes.html',
                           quotations=mongo.db.quotations.find())


@app.route('/add_quote')
def add_quote():
    return render_template('addquote.html',
                           categories=mongo.db.categories.find())


@app.route('/insert_quote', methods=['POST'])
def insert_quote():
    quotes = mongo.db.quotations
    quotes.insert_one(request.form.to_dict())
    return redirect(url_for('get_quotes'))


@app.route('/edit_quote/<quote_id>')
def edit_quote(quote_id):
    the_quote = mongo.db.quotations.find_one({"_id": ObjectId(quote_id)})
    all_categories = mongo.db.categories.find()
    return render_template('editquote.html', quote=the_quote,
                           categories=all_categories)


@app.route('/update_quote/<quote_id>', methods=["POST"])
def update_quote(quote_id):
    quote = mongo.db.quotations
    quote.replace_one({'_id': ObjectId(quote_id)},
                  {
                    'category_name': request.form.get('category_name'),
                    'quotation_text': request.form.get('quotation_text'),
                    'person': request.form.get('person'),
                    'date_said': request.form.get('date_said'),
                    'is_favorite': request.form.get('is_favorite')
                  })
    return redirect(url_for('get_quotes'))


@app.route('/delete_quote/<quote_id>')
def delete_quote(quote_id):
    mongo.db.quotations.remove({'_id': ObjectId(quote_id)})
    return redirect(url_for('get_quotes'))


@app.route('/get_categories')
def get_categories():
    return render_template('categories.html',
                           categories=mongo.db.categories.find())


@app.route('/edit_category/<category_id>')
def edit_category(category_id):
    return render_template('editcategory.html',
                           category=mongo.db.categories.find_one(
                           {'_id': ObjectId(category_id)}))


@app.route('/update_category/<category_id>', methods=['POST'])
def update_category(category_id):
    mongo.db.categories.update(
        {'_id': ObjectId(category_id)},
        {'category_name': request.form.get('category_name')})
    return redirect(url_for('get_categories'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
