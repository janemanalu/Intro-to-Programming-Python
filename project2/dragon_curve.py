import stdio
import sys

# accept n(int) as  command line argument
n = int(sys.argv[1])

# set dragon and nogard as 'F' as the start point
dragon = 'F'
nogard = 'F'

# for all i in the range, change the value of dragon and nogard to what is asked on the writeup
for i in range(1, n + 1):
    dragon2 = dragon
    nogard2 = nogard
    dragon = dragon2 + 'L' + nogard2
    nogard = dragon2 + 'R' + nogard2

# write dragon to standard output
stdio.writeln(dragon)
