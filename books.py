from flask import Flask, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/books_db'
mongo = PyMongo(app)

@app.route('/books/<book_title>', methods=['GET'])
def get_book(book_title):
    book = mongo.db.books.find_one({'title': book_title})
    if book:
        return jsonify({"title": book['title'], "author": book['author']})
    else:
        return jsonify({"error": "Book not found"}), 404

if __name__ == '__main__':
    app.run(port=5001)
