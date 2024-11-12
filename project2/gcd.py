import stdio
import sys

# accept p(int) and q(int) as  command line arguments
p = int(sys.argv[1])
q = int(sys.argv[2])

# while true, run the equation to find q (the gcd)
while p % q != 0:
    p2 = p
    p = q
    q = p2 % q

# write q to standard output
stdio.writeln(q)
