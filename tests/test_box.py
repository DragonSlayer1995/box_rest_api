from app.helpers.validator import is_guid_valid, validate_box_name, validate_cyrillic
from app.models.box import get_age_days
from tests.test_data.box_test_data import BOXES
from tests.helpers.wrong_box_assert_helper import wrong_box_assert

import pytest


def test_positive_get_box(box_client, expected_box_data):
    resp = box_client.get_box('2f11868c-a367-48dc-b4d1-c6706f5258f4')
    resp.check_status(200)
    resp.exact_body(expected_box_data)


def test_get_not_existing_box(box_client):
    resp = box_client.get_box('2f11868c-a367-48dc-b4d1-c6706f5258f5')
    resp.check_status(404)


def test_get_box_by_invalid_id(box_client):
    resp = box_client.get_box('2f11868c')
    resp.check_status(400)


def test_box_guid_after_get(box_client):
    response = box_client.get_box('2f11868c-a367-48dc-b4d1-c6706f5258f4')
    guid = response.body()['id']
    assert is_guid_valid(guid), f'Extracted GUID is not valid!. Extracted GUID: {guid}'


def test_box_name_after_get(box_client):
    response = box_client.get_box('2f11868c-a367-48dc-b4d1-c6706f5258f4')
    name = response.body()['name']
    assert validate_box_name(name), f'Extracted name is not valid!. Extracted name: {name}'


def test_box_cyrillic_after_get(box_client):
    response = box_client.get_box('2f11868c-a367-48dc-b4d1-c6706f5258f4')
    name = response.body()['name']
    assert validate_cyrillic(name), f'Extracted name is not valid!. Extracted name: {name}'


def test_create_box(box_client, box_data):
    create_box_resp = box_client.create_box(box_data)
    guid = create_box_resp.text()
    expected_box = {'id': guid, 'name': box_data['name'],
                    'age_days': get_age_days(box_data['make_date'])}
    get_box_resp = box_client.get_box(guid)

    create_box_resp.check_status(200)
    assert is_guid_valid(guid), f'Extracted GUID is not valid!. Extracted GUID: {guid}'

    get_box_resp.check_status(200)
    get_box_resp.exact_body(expected_box)


@pytest.mark.parametrize('box_data', BOXES)
def test_create_wrong_box(box_client, box_data):
    create_box_resp = box_client.create_box(box_data)
    resp = create_box_resp.text()
    create_box_resp.check_status(400)
    wrong_box_assert(box_data, resp)


def test_delete_box(box_client):
    response = box_client.delete_box('2f11868c-a367-48dc-b4d1-c6706f5258f4')
    response.check_status(200)


@pytest.mark.parametrize('guid, status_code', (('2f11868c-a367-48dc-b4d1-c6706f5258f5', 404), ('2f11868c', 400)))
def test_delete_box_negative(guid, status_code, box_client):
    response = box_client.delete_box(guid)
    response.check_status(status_code)


def test_end_to_end(box_client, box_data):
    create_response = box_client.create_box(box_data)
    guid = create_response.text()
    expected_box = {'id': guid, 'name': box_data['name'],
                    'age_days': get_age_days(box_data['make_date'])}
    get_response = box_client.get_box(guid)

    create_response.check_status(200)
    assert is_guid_valid(guid), f'Extracted GUID is not valid!. Extracted GUID: {guid}'

    get_response.check_status(200)
    get_response.exact_body(expected_box)

    delete_response = box_client.delete_box(guid)
    delete_response.check_status(200)
