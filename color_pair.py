import color_code as g

def get_color_from_pair_number(pair_number):
  zero_based_pair_number = pair_number - 1
  major_index = zero_based_pair_number // g.get_length_major_colors()
  if major_index >= g.get_length_major_colors():
    raise Exception('Major index out of range')
  minor_index = zero_based_pair_number % g.get_length_minor_colors()
  if minor_index >= g.get_length_minor_colors():
    raise Exception('Minor index out of range')
  return g.get_major_colors_index(major_index), g.get_minor_colors_index(minor_index)

def get_pair_number_from_color(major_color, minor_color):
  try:
    major_index = g.get_major_colors_value(major_color)
  except ValueError:
    raise Exception('Major index out of range')
  try:
    minor_index = g.get_minor_colors_value(minor_color)
  except ValueError:
    raise Exception('Minor index out of range')
  return major_index * g.get_length_minor_colors() + minor_index + 1
