import sys

# Enter a number in the Command line arguments (50 10)
sys.stdin = (sys.argv[1])
sys.stdin = (sys.argv[2])

def quotient(a, b):
  return a // b
 
# Read data from arguments
a = int(sys.argv[1])
b = int(sys.argv[2])

print(f'Quotient of {a} and {b} is {quotient(a, b)}')