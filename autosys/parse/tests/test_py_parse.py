from ..py_parse import identifier

test_list: List[str] = [
    'This is a test.',
    'identifier',
    'python',
    '_LowerCASE',
    'number38463',
    'num_ber_fk38834_00234',
    '',
    '9fksdjf',
    '   fsd keywords\n'
]


def test_identifier():
    for s in test_list:
        assert s.isidentifier()
        print(s.isidentifier())
