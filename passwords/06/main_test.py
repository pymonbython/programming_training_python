from main import connect_ext_api


def test_true(requests_mock):
    # Przeciążmy metodę get
    data = '00264A0EA456B57A3FC7258B13F3D29B3C0:6\n00294015E5A8513C73396D18309F3FFF34A:8'
    requests_mock.get('https://api.pwnedpasswords.com/range/A94A8', text=data)
    assert connect_ext_api(10) == False

def test_false(requests_mock):
    # Przeciążmy metodę get
    data = '00264A0EA456B57A3FC7258B13F3D29B3C0:11\n00294015E5A8513C73396D18309F3FFF34A:8'
    requests_mock.get('https://api.pwnedpasswords.com/range/A94A8', text=data)
    assert connect_ext_api(10) == True
