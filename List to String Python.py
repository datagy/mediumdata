our_list = ['I','am', 'learning', 'Python', 'with', 'datagy!']

def spaces(your_list):
  """Delimit your list by spaces."""
  return ' '.join(your_list)

space_string = spaces(our_list)
print("Our list delimited by spaces:")
print(space_string)

def commas(your_list):
  """Delimit your list by commas."""
  return ','.join(your_list)

comma_string = commas(our_list)
print("Our list delimited by commas:")
print(comma_string)

def new_lines(your_list):
  """Delimit your list by new lines."""
  return '\n'.join(your_list)

new_lines_string = new_lines(our_list)
print("Our list delimited by new lines:")
print(new_lines_string)
