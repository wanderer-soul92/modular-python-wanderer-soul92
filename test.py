import color_pair
import color_codes as g

def test_number_to_pair(pair_number,
                        expected_major_color, expected_minor_color):
  major_color, minor_color = color_pair.get_color_from_pair_number(pair_number)
  assert(major_color == expected_major_color)
  assert(minor_color == expected_minor_color)


def test_pair_to_number(major_color, minor_color, expected_pair_number):
  pair_number = color_pair.get_pair_number_from_color(major_color, minor_color)
  assert(pair_number == expected_pair_number)

def test_user_manual_length(expected_pair_count):
    user_manual_length = len(g.get_user_manual())
    assert(user_manual_length == expected_pair_count)
