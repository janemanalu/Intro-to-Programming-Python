import stdio
import sys

# accept n(int) as  command line argument
n = int(sys.argv[1])

# a and b as the first two fibonacci number and i as the ith fibonacci number
a = 1
b = 1
i = 3

# while true, run the calculation to find b(nth fibonacci number)
while i <= n:
    a2 = a
    a = b
    b = a2 + b
    i += 1

# write b to standard output
stdio.writeln(b)
