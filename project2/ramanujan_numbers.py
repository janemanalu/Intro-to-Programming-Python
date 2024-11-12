import stdio
import sys

# accept n(int) as  command line argument
n = int(sys.argv[1])

# set a, b, c, d, to the lower bound of each of their conditions, and apply while loop to each of them for the upper
# bound. If out of the bounds, increment a/b/c/d by 1
a = 1
while a * a * a <= n:
    b = a + 1
    while b * b * b <= (n - a**3):
        c = a + 1
        while c * c * c <= n:
            d = c + 1
            while d * d * d <= (n - c**3):

                # if true write the desired output
                if a * a * a + b * b * b == c * c * c + d * d * d:
                    total = a * a * a + b * b * b
                    stdio.writeln(str(total) + ' = ' + str(a) + '^3 + ' + str(b) + '^3 = ' + str(c) + '^3 + ' + str(d)
                                  + '^3')
                d += 1
            c += 1
        b += 1
    a += 1
