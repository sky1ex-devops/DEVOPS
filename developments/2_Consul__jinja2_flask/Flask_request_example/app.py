from flask import Flask, jsonify, request
 
app = Flask(__name__)
 
data = {
    "users": [
        {"id": 1, "name": "John"},
        {"id": 2, "name": "Jane"},
    ]
}
 
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(data["users"])
 
@app.route('/users/&lt;int:user_id&gt;', methods=['GET'])
def get_user(user_id):
    user = next((u for u in data["users"] if u["id"] == user_id), None)
    if user is None:
        return "User not found", 404
    return jsonify(user)
 
@app.route('/users', methods=['POST'])
def create_user():
    user = request.get_json()
    data["users"].append(user)
    return jsonify(user), 201
 
@app.route('/users/&lt;int:user_id&gt;', methods=['DELETE'])
def delete_user(user_id):
    user = next((u for u in data["users"] if u["id"] == user_id), None)
    if user is None:
        return "User not found", 404
    data["users"].remove(user)
    return "User deleted", 204
 
if __name__ == '__main__':
    app.run()