def break_string(string, chunk_size=8):
  """Breaks a string into lines of a specified chunk size.

  Args:
    string: The string to be broken.
    chunk_size: The desired size of each line.

  Returns:
    A list of strings, each representing a line.
  """

  return [string[i:i+chunk_size] for i in range(0, len(string), chunk_size)]


def print_broken_string(string, chunk_size=8):
  """Breaks a string into lines of a specified chunk size and prints them.

  Args:
    string: The string to be broken and printed.
    chunk_size: The desired size of each line.
  """

  broken_lines = [string[i:i+chunk_size] for i in range(0, len(string), chunk_size)]
  for line in broken_lines:
    print(line)

"""# Example usage:
my_string = "This is a long string to be broken."
print_broken_string(my_string)
# Example usage:
my_string = "This is a long string to be broken."
broken_lines = break_string(my_string)

for line in broken_lines:
  print(line)"""