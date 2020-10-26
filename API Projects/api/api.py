import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# create some data for displaying 
books = [
    {'id': 0,
    'title': 'A Fire Upon the Deep',
    'author': 'James Stewart',
    'year_published': '1995'},
    {'id': 1,
    'title': 'Into the Wood',
    'author': 'Jon Milney',
    'year_published': '2000'},
    {'id': 2,
    'title': 'A Blazing Women',
    'author': 'Alice',
    'year_published': '1885'}
]

@app.route('/', methods = ['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading  of science fiction novels</p>"


# A route to return the books details
@app.route('/api/v1/resources/books/all', methods = ['GET'])
def api_all():
    return jsonify(books)

# above shows all the database to the user lets show user what they want only
# finding resources
@app.route('/api/v1/resources/books', methods = ['GET'])
def api_id():
    # if id has been provided in url get it else return ERRO
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return 'ERROR! No id provided. Please specify an id.'
    
    # create empty list for our results
    results = []

    # search for the id in database
    for book in books:
        if book['id'] == id:
            results.append(book)

    return jsonify(results)
# Enter the url - 127.0.0.1:5000/api/v1/resources/books?id=0 127.0.0.1:5000/api/v1/resources/books?id=1

# run the app
app.run()