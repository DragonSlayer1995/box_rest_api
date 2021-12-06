import re
from datetime import datetime, timedelta
from box import Box

first_box = Box('2f11868c-a367-48dc-b4d1-c6706f5258f4', 'simple box', 12, '2021-10-15')

ALL_BOXES = {
    first_box.id: first_box
}


def is_guid_valid(guid):
    guid_pattern = re.compile(r'^[\da-f]{8}-([\da-f]{4}-){3}[\da-f]{12}$', re.IGNORECASE)
    return True if guid_pattern.match(guid) else False


def validate_box_name(box_name):
    result = False
    if box_name:
        if 5 <= len(box_name) <= 30:
            result = True
    return result


def validate_box_make_date(box_make_date):
    result = False
    current_date = datetime.today().date()
    current_date_minus_year = current_date - timedelta(days=365)
    if box_make_date:
        make_date = datetime.strptime(box_make_date, '%Y-%m-%d').date()
        if current_date_minus_year <= make_date <= current_date:
            result = True
    return result


def validate_box(name, date):
    name_result = validate_box_name(name)
    date_result = validate_box_make_date(date)
    failed_fields = []
    if all([name_result, date_result]):
        return True,
    else:
        if not validate_box_name(name):
            failed_fields.append('name')
        if not validate_box_make_date(date):
            failed_fields.append('make_date')
        return False, failed_fields
