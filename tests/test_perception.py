from perception.object_detection import detect_object

def test_perception():
    assert detect_object(100) is True