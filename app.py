from flask import Flask, jsonify, request
app = Flask(__name__)
inventory = {}
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(list(inventory.values()))

@app.route('/items/<item_id>', methods=['GET'])
def get_item(item_id):
    if item_id not in inventory:
        return jsonify({"error": "Not found"}), 404
    return jsonify(inventory[item_id])

@app.route('/items', methods=['POST'])
def add_item():
    data = request.json
    inventory[data['id']] = data
    return jsonify(data), 201

if __name__ == '__main__':
    app.run()
