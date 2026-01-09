from standard_calc import bound_to_180, is_angle_between


DELTA = 1e-6

""" Tests for bound_to_180() """
def test_bound_basic1():
    cases = [
        (0.0, 0.0),
        (91.0, 91.0),
        (180.0, -180.0),
        (180.1, -179.9), 
        (-180.0, -180.0),
        (-180.5, 179.5),
        (359.5, -0.5),
        (360.0, 0.0),
        (200, -160),
        (-67.0, -67.0),
        (-300.55, 59.45),
        (638.22, -81.78),
        (-711.3, 8.7)
    ]

    for input, expected in cases:
        assert abs(bound_to_180(input) - expected) < DELTA


""" Tests for is_angle_between() """
def test_between_basic1():
    cases = [
        (0, 1, 2, True),
        (1, 1, 1, True),
        (0, 300, 270, True),
        (-1, -30, -150, True),
        (1, 0.1, -1, True),
        (360, 45, 90, True),
        (90, 95+360, 100, True),
        (0, 100, 10, False),
        (-40, -50, -30, False),
        (180, 10, 90, False), 
        (1, 1.1, 1, False),
        (30, 90.01, 90, False),

        (0, 90, 180, True), 
        (0, 270, 180, True)
    ]

    for f, m, s, expected in cases:
        assert is_angle_between(f, m, s) == expected
