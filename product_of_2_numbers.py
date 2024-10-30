import sys

# Enter a number in the Command line arguments (10 2)
sys.stdin = (sys.argv[1])
sys.stdin = (sys.argv[2])

def product(a, b):
  return a * b
 
# Read data from arguments
a = int(sys.argv[1])
b = int(sys.argv[2])

print(f'Product of {a} and {b} is {product(a, b)}')