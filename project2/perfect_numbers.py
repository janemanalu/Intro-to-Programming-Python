import stdio
import sys

# accept n(int) as  command line argument
n = int(sys.argv[1])

# for all i in the range, run the j for-loop
for i in range(2, n + 1):

    # set total to zero as a starting point
    total = 0

    # for all j in the range, run the calculation to increase total by j if j divides i
    for j in range(1, i // 2 + 1):
        if i % j == 0:
            total += j
           

    # when total becomes i, write i to standard output
    if total == i:
        stdio.writeln(i)
