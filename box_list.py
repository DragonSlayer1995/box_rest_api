import re
from uuid import UUID
from box import Box

first_box = Box('2f11868c-a367-48dc-b4d1-c6706f5258f4', 'simple box', 12, '2021-10-15')

ALL_BOXES = {
    first_box.id: first_box
}


def is_guid_valid(guid):
    guid_pattern = re.compile(r'^[\da-f]{8}-([\da-f]{4}-){3}[\da-f]{12}$', re.IGNORECASE)
    return True if guid_pattern.match(guid) else False
