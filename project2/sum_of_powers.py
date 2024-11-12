import stdio
import sys

# # accept n(int) and k(int) as  command line arguments
n = int(sys.argv[1])
k = int(sys.argv[2])

# set total to zero as the start
total = 0

# for all (a) in the range, total increase with i to the power of k
for i in range(1, n+1):
    total += i**k

# write total to standard output
stdio.writeln(total)
