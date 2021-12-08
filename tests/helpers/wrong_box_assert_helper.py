def wrong_box_assert(box, resp):
    if box['box_type'] == 'bad_box':
        assert 'name' in resp and 'make_date' in resp, \
            'Wrong response! name and make_date parameters should be in response!'
    if box['box_type'] == 'bad_name_box':
        assert 'name' in resp, 'Wrong response! name parameter should be in response!'
    if box['box_type'] == 'bad_make_date_box':
        assert 'make_date' in resp, 'Wrong response! make_date parameter should be in response!'
