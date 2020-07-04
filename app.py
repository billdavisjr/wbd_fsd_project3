import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'quotations_space'
app.config["MONGO_URI"] = os.getenv('MONGO_URI')


mongo = PyMongo(app)


@app.route('/')
@app.route('/get_quotes')
def get_quotes():
    return render_template('quotes.html',
                           quotations=mongo.db.quotations.find().sort("person"))


@app.route('/search_quotes', methods=['POST'])
def search_quotes():
    search_text = request.form.get('searchfield')
    if search_text == '':
        return render_template('quotes.html',
                               quotations=mongo.db.quotations.find().sort("person"),
                               searchfield=search_text)
    else:
        the_search = {'$text': {'$search': search_text}}
        print('Search string:')
        print(the_search)
        search_results = mongo.db.quotations.find(the_search).sort("person")
        return render_template('quotes.html',
                               quotations=search_results,
                               searchfield=search_text)


@app.route('/add_quote')
def add_quote():
    return render_template('addquote.html',
                           categories=mongo.db.categories.find().sort("category_name"))


@app.route('/insert_quote', methods=['POST'])
def insert_quote():
    quotes = mongo.db.quotations
    quotes.insert_one(request.form.to_dict())
    return redirect(url_for('get_quotes'))


@app.route('/edit_quote/<quote_id>')
def edit_quote(quote_id):
    the_quote = mongo.db.quotations.find_one({"_id": ObjectId(quote_id)})
    all_categories = mongo.db.categories.find().sort("category_name")
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
                        'source': request.form.get('source'),
                        'date_said': request.form.get('date_said'),
                        'stars_rating': request.form.get('stars_rating'),
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
                            categories=mongo.db.categories.find().sort("category_name"))


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


@app.route('/delete_category/<category_id>')
def delete_category(category_id):
    mongo.db.categories.remove({'_id': ObjectId(category_id)})
    return redirect(url_for('get_categories'))


@app.route('/insert_category', methods=['POST'])
def insert_category():
    category_doc = {'category_name': request.form.get('category_name')}
    mongo.db.categories.insert_one(category_doc)
    return redirect(url_for('get_categories'))


@app.route('/add_category')
def add_category():
    return render_template('addcategory.html')


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    host = os.environ.get('IP')
    port = int(os.environ.get('PORT'))
    debug = True
    app.run(host, port, debug)
