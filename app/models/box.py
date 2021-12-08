import uuid
from dataclasses import dataclass
from datetime import datetime
from flask import Response
from app.helpers.validator import validate_box, is_guid_valid


@dataclass()
class Box:
    id: str
    name: str
    age_days: int
    make_date: str


ALL_BOXES = {
    '2f11868c-a367-48dc-b4d1-c6706f5258f4': Box('2f11868c-a367-48dc-b4d1-c6706f5258f4', 'просто коробка', 12, '2021-10-15')
}


def create_new_box(body):
    validation_result = validate_box(body['name'], body['make_date'])
    if validation_result[0]:  # 0 - bool result
        age_days = get_age_days(body['make_date'])
        box = Box(str(uuid.uuid4()), body['name'], age_days, body['make_date'])
        ALL_BOXES[box.id] = box
        return box.id
    else:
        return Response(f"Problems with the next fields: {validation_result[1]}",  # 1 - list of failed fields
                        status=400)


def get_box(box_id):
    if not is_guid_valid(box_id):
        return Response(status=400)
    if box_id not in ALL_BOXES:
        return Response(status=404)
    box = ALL_BOXES[box_id]
    return {
        'id': box.id,
        'name': box.name,
        'age_days': box.age_days
    }


def delete_box(box_id):
    if is_guid_valid(box_id):
        if box_id in ALL_BOXES:
            del ALL_BOXES[box_id]
            return Response(status=200)
        else:
            return Response(status=404)
    else:
        return Response(status=400)


def get_age_days(make_date):
    make_date = datetime.strptime(make_date, '%Y-%m-%d').date()
    current_date = datetime.today().date()
    age_days = (current_date - make_date).days
    return age_days
