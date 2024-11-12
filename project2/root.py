import stdio
import sys

# accept k(int), c(float), epsilon(float) as  command line arguments
k = int(sys.argv[1])
c = float(sys.argv[2])
epsilon = float(sys.argv[3])

# t (the guess of root result), c (the number that the root want to be found)
t = c

# While true, using the equation to find the result of the root
while abs(1 - (c/(t**k))) > epsilon:
    t2 = t
    ft = t ** k - c
    f_prime_t = k * (t ** (k - 1))
    t = t2 - ft/f_prime_t

# write t to standard output
stdio.writeln(t)
