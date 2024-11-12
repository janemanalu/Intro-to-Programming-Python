import stdio
import sys

# accepts two command line arguments, t(temp) and v(speed)
t = float(sys.argv[1])
v = float(sys.argv[2])

# the equation to find the effective temperature (the wind chill)
w = 35.74 + 0.6215 * t + (0.4275 * t - 35.75) * (v**0.16)

# conditions for the equation to work, temp needs to be more than 50 Fahrenheit and speed needs to be
# less than equal to 3, write desired output to standard output (depends on which condition is True)
if t > 50:
    stdio.writeln('Value of t must be <= 50 F')
elif v <= 3:
    stdio.writeln('Value of v must be > 3 mph')
else:
    stdio.writeln(w)
