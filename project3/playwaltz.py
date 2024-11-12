
import stdaudio
import stdio
import sys

# receiving the waltz measures, minuet and trio, from the standard input(output of generatewaltz.py)
measures = []
measures += stdio.readAllInts()

# three errors that must be followed regarding the number and the value of each measure
if len(measures) != 32:
    sys.exit('A waltz must contain exactly 32 measures')
else:
    for M in measures[0:16]:
        if M < 1 or M > 176:
            sys.exit('A minuet measure must be from [1, 176]')

    for T in measures[16:32]:
        if T < 1 or T > 96:
            sys.exit('A trio measure must be from [1, 96]')

# write the standard output of playing the sound of each file from the minuet measure and trio measure
for M in measures[0:16]:
    # data name = data/M(int)
    stdaudio.playFile('data/M' + str(M))

for T in measures[16:32]:
    stdaudio.playFile('data/T' + str(T))

# wait until the song is finished
stdaudio.wait()

