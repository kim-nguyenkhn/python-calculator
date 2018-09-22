import sys

def sum(x, y):
  return x + y

def multiply(x, y):
  return x * y

methods = {
  'sum': sum,
  'multiply': multiply
}

# Extract arguments
list_of_args = sys.argv[1:]
method = methods[list_of_args[0]]  # 'sum', 'multiply'
x = int(list_of_args[1])
y = int(list_of_args[2])

# print "method: %s\nx: %s\ny: %s" % (method, x, y)

print method(x, y)

'''
Tasks:
- Implement subtraction, division, and any other calculations.
- Refactor this into a class implementation.
- Make the script more "interactive" - users shouldn't have to memorize the method names.
'''
