import stdio
import sys

# accept m(int), d(int), y(int) as  command line arguments represents a date
m = int(sys.argv[1])
d = int(sys.argv[2])
y = int(sys.argv[3])

# equation to find the day of the week (0 for sunday, 1 for monday, etc.)
y0 = y - (14 - m) // 12
x0 = y0 + y0 // 4 - y0 // 100 + y0 // 400
m0 = m + 12 * ((14 - m) // 12) - 2
dow = (d + x0 + 31 * m0 // 12) % 7

# Changing the value of dow from int to str, following the pairs on the writeup.
if dow == 0:
    dow = 'Sunday'
elif dow == 1:
    dow = 'Monday'
elif dow == 2:
    dow = 'Tuesday'
elif dow == 3:
    dow = 'Wednesday'
elif dow == 4:
    dow = 'Thursday'
elif dow == 5:
    dow = 'Friday'
elif dow == 6:
    dow = 'Saturday'

# write dow to standard output
stdio.writeln(dow)
