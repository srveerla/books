from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rentings.db'
db = SQLAlchemy(app)

class Renting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    book_id = db.Column(db.Integer, nullable=False)
    start_date = db.Column(db.String(20), nullable=False)
    end_date = db.Column(db.String(20), nullable=False)

@app.route('/rentings', methods=['GET'])
def get_rentings():
    rentings = Renting.query.all()
    return jsonify({"rentings": [{"id": renting.id, "user_id": renting.user_id, "book_id": renting.book_id, "start_date": renting.start_date, "end_date": renting.end_date} for renting in rentings]})

@app.route('/rentings', methods=['POST'])
def create_renting():
    data = request.get_json()

    # Validate user
    user_id = data.get('userId')
    if not User.query.get(user_id):
        return jsonify({"error": "User not found"}), 404

    # Validate book
    book_id = data.get('bookId')
    if not Book.query.get(book_id):
        return jsonify({"error": "Book not found"}), 404

    # Create renting record
    renting_record = Renting(user_id=user_id, book_id=book_id, start_date=data.get("startDate"), end_date=data.get("endDate"))
    db.session.add(renting_record)
    db.session.commit()

    return jsonify({"renting": {"id": renting_record.id, "user_id": renting_record.user_id, "book_id": renting_record.book_id, "start_date": renting_record.start_date, "end_date": renting_record.end_date}}), 201

if __name__ == '__main__':
    db.create_all()
    app.run(port=5002)
