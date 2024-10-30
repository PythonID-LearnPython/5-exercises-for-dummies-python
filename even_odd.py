import sys

# Enter a number in the Command line arguments
sys.stdin = (sys.argv[1])

# Read data from arguments
number = int(sys.argv[1])

# Check if the number you just entered is even or odd
if number % 2 == 0:
    print("even")
else:
    print("odd")
