# connect to database and show the results
# database name - books.db

from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
app.config["DEBUG"] = True

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]

    return d


@app.route('/', methods = ['GET'])
def home():
    return ''' <h1> Distant Reading Archive</h1>
                <p> A Prototype API for science fiction novels</p> '''

@app.route('/api/v1/resources/books/all', methods = ['GET'])
def api_all():
    '''function return the all books name'''

    # connect to database
    connection = sqlite3.connect('books.db')
    cur = connection.cursor()

    # get all books
    all_books = cur.execute("SELECT * FROM books;").fetchall()
    return jsonify(all_books)


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404 NOT FOUND</h1>", 404

# get specific book
@app.route('/api/v1/resources/books', methods = ['GET'])
def api_filter():
    '''function to show only what user wants'''

    query_parameters = request.args
    id = query_parameters.get('id')
    published = query_parameters.get('published')
    author = query_parameters.get('author')

    query = 'SELECT * FROM books WHERE'
    to_filter = []

    if id:
        query += ' id=? AND'
        to_filter.append(id)
    if published:
        query += ' published=? AND'
        to_filter.append(published)
    if author:
        query += ' author=? AND'
        to_filter.append(author)
    
    if not(id or published or author):
        return page_not_found(404)

    query = query[:-4] + ';'

    # connect to database
    connection = sqlite3.connect('books.db')
    #connection.row_factory = dict_factory
    cur = connection.cursor()

    results = cur.execute(query, to_filter).fetchall()

    return jsonify(results)

# Test url - http://127.0.0.1:5000/api/v1/resources/books?author=Connie+Willis&published=1993

app.run()
