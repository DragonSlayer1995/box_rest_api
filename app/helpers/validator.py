import re
from datetime import datetime, timedelta


def is_guid_valid(guid):
    guid_pattern = re.compile(r'^[\da-f]{8}-([\da-f]{4}-){3}[\da-f]{12}$', re.IGNORECASE)
    return True if guid_pattern.match(guid) else False


def validate_box_name(box_name):
    result = False
    if box_name and validate_cyrillic(box_name):
        if 5 <= len(box_name) <= 20:
            result = True
    return result


def validate_box_make_date(box_make_date):
    result = False
    current_date = datetime.today().date()
    current_date_minus_year = current_date - timedelta(days=365)
    if box_make_date:
        try:
            make_date = datetime.strptime(box_make_date, '%Y-%m-%d').date()
        except ValueError:
            return result
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


def validate_cyrillic(text):
    alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя123456789 '
    return all([letter in alphabet for letter in text])
