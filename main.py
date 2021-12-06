from flask import Flask, abort, request
from box_list import ALL_BOXES, is_guid_valid

app = Flask(__name__)


@app.route('/api/box/<string:box_id>', methods=['GET'])
def get_box_by_id(box_id):
    if not is_guid_valid(box_id):
        abort(400)
    if box_id not in ALL_BOXES:
        abort(404)
    box = ALL_BOXES[box_id]

    return {
        'id': box.id,
        'name': box.name,
        'age_days': box.age_days
    }


@app.route('/api/box', methods=['POST'])
def create_box():
    body = request.get_json()


if __name__ == '__main__':
    app.run(debug=True)
