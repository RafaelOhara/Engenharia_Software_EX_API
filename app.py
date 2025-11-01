from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

items = [
    {'id': 1, 'name': 'item 1'},
    {'id': 2, 'name': 'item 2'}]
@app.route('/item',methods=['GET'])
def get_item():
    return jsonify({"item": items})

@app.route('/item/<int:item_id>',methods=['GET'])
def get_item_by_id(item_id):
    item = next((i for i in items if i['id'] == item_id), None)
    if item:
        return jsonify({'item':item})
    return jsonify({'error': 'item nao existe'})

@app.route('/item',methods=['POST'])
def creat_item():
    new_item = {'id': len(items) + 1, "name": request.json["name"]}
    items.append(new_item)
    return jsonify({'item': new_item}),201

@app.route('/item/<int:item_id>',methods=['PUT'])
def put_item_by_id(item_id):
    item = next((i for i in items if i['id'] == item_id), None)
    if item:
        item['name'] = request.json['name']
        return jsonify({'item': item})
    return jsonify({'error': 'item nao existe'}),404
@app.route('/item/<int:item_id>',methods=['DELETE'])
def delete_item_by_id(item_id):
    global items
    items = [i for i in items if i['id'] != item_id]
    return jsonify({'resultado': True})


if __name__ == '__main__':
    app.run(debug=True)