import test

def color_pair_to_string(major_color, minor_color):
  return f'{major_color} {minor_color}'

if __name__ == '__main__':
  test.test_number_to_pair(4, 'White', 'Brown')
  test.test_number_to_pair(5, 'White', 'Slate')
  test.test_pair_to_number('Black', 'Orange', 12)
  test.test_pair_to_number('Violet', 'Slate', 25)
  test.test_pair_to_number('Red', 'Orange', 7)
  print('Done :)')
