import sys

# Enter a number in the Command line arguments (10 2)
sys.stdin = (sys.argv[1])
sys.stdin = (sys.argv[2])

def Difference(a, b):
  return a - b
 
# Read data from arguments
a = int(sys.argv[1])
b = int(sys.argv[2])

print(f'Difference  of {a} and {b} is {Difference(a, b)}')