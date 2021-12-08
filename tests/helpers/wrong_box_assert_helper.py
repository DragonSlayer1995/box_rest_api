def wrong_box_assert(box, text):
    if 'name' in box['box_type']:
        assert 'name' in text, 'Wrong response! name parameter should be in response!\n Response text ' + text
    elif 'make_date' in box['box_type']:
        assert 'make_date' in text, 'Wrong response! make_date parameter should be in response!\n Response text ' + text
    else:
        assert 'name' in text and 'make_date' in text, \
            'Wrong response! name and make_date parameters should be in response!\n Response text ' + text


