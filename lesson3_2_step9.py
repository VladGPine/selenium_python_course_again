def assertion_func(fulltext, some_value):
    assert some_value in fulltext, f'expected {some_value} to be substring of {fulltext}'


assertion_func('some_text', 'some')
