from flask import Flask, abort, request, Response
from box_list import ALL_BOXES, is_guid_valid, validate_box

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
        validation_result = validate_box(body['name'], body['make_date'])
        if validation_result[0]:  # 0 - bool result
            return Response(status=200)
        else:
            return Response(f"Problems with the next fields: {validation_result[1]}",  # 1 - list of failed fields
                            status=400)


if __name__ == '__main__':
    app.run(debug=True)
