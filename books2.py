from flask import Flask, request, jsonify

app = Flask(__name__)

# Books database
books = {}

# Add a new book to the catalog
@app.route("/books", methods=["POST"])
def add_book():
    book_data = request.get_json()
    book_id = book_data["book_id"]
    title = book_data["title"]
    author = book_data["author"]
    genre = book_data["genre"]

    books[book_id] = {
        "title": title,
        "author": author,
        "genre": genre,
        "status": "available"
    }

    return jsonify({
        "success": True,
        "message": "Book added to the catalog successfully."
    })

# Get all books in the catalog
@app.route("/books", methods=["GET"])
def get_all_books():
    return jsonify({
        "success": True,
        "books": books
    })

# Get a specific book from the catalog
@app.route("/books/<book_id>", methods=["GET"])
def get_book(book_id):
    if book_id not in books:
        return jsonify({
            "success": False,
            "message": "Book does not exist."
        })

    return jsonify({
        "success": True,
        "book": books[book_id]
    })

if __name__ == "__main__":
    app.run(debug=True)
