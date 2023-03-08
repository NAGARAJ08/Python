from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def start_page():
    return "Welcome to eShopping"


Shopping_list = [
    {
        "_id": "U1IT00010",
        "item_name": "blender",
        "max_discount": "10%",
        "batch_number": "RR450020FRG",
        "price": 340
    },
    {
        "_id": "U1IT00001",
        "item_name": "Blender",
        "max_discount": "10%",
        "batch_number": "RR450020FRG",
        "price": 340,
        "category": "kitchen appliance"
    },
    {
        "_id": "U1IT00002",
        "item_name": "Egg",
        "category": "food",
        "quantity": 12,
        "price": 36,
        "item_description": "brown country eggs"
    },
    {
        "_id": "BF00001CFOOD",
        "item_name": "Bread",
        "quantity": 2,
        "ingredients": "all-purpose flour"
    }
]


# http://127.0.0.1:5000/Shopping_list
@app.route('/Shopping_list', methods=['GET'])
def get_shopping_list():
    return jsonify(Shopping_list)


# this method return a particular item
# http://127.0.0.1:5000/Shopping_list/Egg
@app.route('/Shopping_list/<string:item>', methods=['GET'])
def return_one_item(item):
    q = Shopping_list[0]
    for i, j in enumerate(Shopping_list):
        if j['item_name'] == item:
            q = Shopping_list[i]
    return jsonify({'item': q})


# http://127.0.0.1:5000/Shopping_list
@app.route('/Shopping_list', methods=['POST'])
def add_shopping_list():
    Shopping_list.append(request.get_json())
    return 'Item Added'


# http://127.0.0.1:5000/Shopping_list/update/Egg
# Edits/Updates information in the Database or else adds it if not present already.

@app.route('/Shopping_list/update/<string:name>', methods=['PUT'])
def editOne(name):
    new_item = request.get_json()
    for i, q in enumerate(Shopping_list):
        if q['item_name'] == name:
            Shopping_list[i] = new_item

    return jsonify({'List': Shopping_list})


# http://127.0.0.1:5000/Shopping_list/delete/Egg
@app.route('/Shopping_list/delete/<string:item>', methods=['DELETE'])
def delete_item(item):
    for i, q in enumerate(Shopping_list):
        if q['item_name'] == item:
            del Shopping_list[i]
    return "its Deleted"


if __name__ == "__main__":
    app.run(debug=True)
