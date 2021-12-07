from flask import Flask, request
from app.models.box import get_box, create_new_box, delete_box

app = Flask(__name__)


@app.route('/api/box/<string:box_id>', methods=['GET'])
def rest_get_box(box_id):
    return get_box(box_id)


@app.route('/api/box', methods=['POST'])
def rest_create_box():
    body = request.get_json()
    return create_new_box(body)


@app.route('/api/box/<string:box_id>', methods=['DELETE'])
def rest_delete_box(box_id):
    return delete_box(box_id)


if __name__ == '__main__':
    app.run(debug=True)
