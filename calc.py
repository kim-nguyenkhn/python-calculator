import sys

def sum(x, y):
  return x + y

def subtract(x,y):
  return x-y

def multiply(x, y):
  return x * y

def divide(x,y):
  return x/y

methods = {
  'sum': sum,
  'subtract': subtract,
  'multiply': multiply,
  'divide': divide
}

# Extract arguments
list_of_args = sys.argv[1:]
method = methods[list_of_args[0]]  # 'sum', 'multiply'
x = int(list_of_args[1])
y = int(list_of_args[2])

# print "method: %s\nx: %s\ny: %s" % (method, x, y)

print method(x, y)
