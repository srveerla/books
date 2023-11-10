from flask import Flask, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/users_db'
mongo = PyMongo(app)

@app.route('/users/<username>', methods=['GET'])
def get_user(username):
    user = mongo.db.users.find_one({'username': username})
    if user:
        return jsonify({"username": user['username'], "email": user['email']})
    else:
        return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(port=5000)
