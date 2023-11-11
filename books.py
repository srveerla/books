from flask import Flask, jsonify, request
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://mongo:27017/library"
mongo = PyMongo(app)

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

@app.route('/books', methods=['GET'])
def get_books():
    books = list(mongo.db.books.find({}, {'_id': 0}))
    return jsonify(books)

@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    book = Book(data['title'], data['author'])
    mongo.db.books.insert_one(book.__dict__)
    return 'Book added', 201

if __name__ == '__main__':
    app.run(host='0.0.0.0')
