from tracker import Tracker

def test_tracker_initialization():
    my_tracker = Tracker({'test'}, 'test')
    assert str(type(my_tracker)) == "<class 'tracker.Tracker'>"

def test_element_counter():
    my_tracker = Tracker({'\\lx', '\\xv'}, '\\lx')
    my_tracker.number_duplicates_in_list(['\\lx', '\\lx', '\\xv', '\\lx'])
    assert my_tracker.element_counter == {'\\lx': 3, '\\xv': 0}

def test_number_duplicates_in_list():
    my_list = ['\\lx', 'Arroyo', '\\ge', 'brook', '\\xv', '', '\\ge', 'stream', '\\xv', 'the stream flows', '\\ge', 'river', '\\ge', 'water', '\\xv', 'water also flows']
    my_tracker = Tracker({'\\ge', '\\xv'}, '\\ge')
    my_tracker.number_duplicates_in_list(my_list)
    assert my_list == ['\\lx', 'Arroyo', '\\ge1', 'brook', '\\xv1', '', '\\ge2', 'stream', '\\xv2', 'the stream flows', '\\ge3', 'river', '\\ge4', 'water', '\\xv4', 'water also flows']

def test_number_duplicates_in_list_with_multiple_examples():
    my_list = ['\\lx', 'Arroyo', '\\ge', 'stream', '\\xv', 'the stream', '\\xv', 'the stream flows', '\\ge', 'water', '\\xv', 'the water is blue', '\\xv', 'the water is green', '\\xv', 'the water is pink', '\\ge', 'brook', '\\xv', 'the brook is flowing']
    my_tracker = Tracker({'\\ge', '\\xv'}, '\\ge')
    my_tracker.number_duplicates_in_list(my_list)
    assert my_list == ['\\lx', 'Arroyo', '\\ge1', 'stream', '\\xv1', 'the stream', '\\xv1-2', 'the stream flows', '\\ge2', 'water', '\\xv2', 'the water is blue', '\\xv2-2', 'the water is green', '\\xv2-3', 'the water is pink', '\\ge3', 'brook', '\\xv3', 'the brook is flowing']

def test_random():
    my_list = ['\\lx', 'Aprender', '\\n', 'new', '\\ge', 'nearby', '\\re', 'nearby', '\\gn', '', '\\dt', '11/Jan/2005', '\\ps', 'v', '\\n', '0281a', '\\ge', '"learn999 teach999 tame"', '\\re', 'learn ; teach ; tame', '\\xv', 'learn is fun', '\\xv', 'learning is good', '\\gn', 'apprendre', '\\dt', '28/Jan/2005']
    my_tracker = Tracker({'\\ge', '\\re', '\\xv'}, '\\ge')
    my_tracker.number_duplicates_in_list(my_list)
    assert my_list == ['\\lx', 'Aprender', '\\n', 'new', '\\ge1', 'nearby', '\\re1', 'nearby', '\\gn', '', '\\dt', '11/Jan/2005', '\\ps', 'v', '\\n', '0281a', '\\ge2', '"learn999 teach999 tame"', '\\re2', 'learn ; teach ; tame', '\\xv2', 'learn is fun', '\\xv2-2', 'learning is good', '\\gn', 'apprendre', '\\dt', '28/Jan/2005']