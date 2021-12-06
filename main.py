from flask import Flask, abort, request, Response
from box_list import ALL_BOXES, is_guid_valid, validate_box_name, validate_box_make_date

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
    if body:
        print('Body is not empty')
        if validate_box_name(body['name']) and validate_box_make_date(body['make_date']):
            return 'box was created'
        else:
            return Response(f"Problems with name: {body['name']}", status=400)


if __name__ == '__main__':
    app.run(debug=True)
