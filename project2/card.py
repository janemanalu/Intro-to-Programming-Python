import stdio
import stdrandom

# setting rank and suit to random integer with their respective range
rank = stdrandom.uniformInt(2, 15)
suit = stdrandom.uniformInt(1, 5)

# using if statement to make rank as string with their pairs that was decided in the writeup
if rank == 11:
    rankStr = 'Jack'
elif rank == 12:
    rankStr = 'Queen'
elif rank == 13:
    rankStr = 'King'
elif rank == 14:
    rankStr = 'Ace'
else:
    rankStr = str(rank)

# using if statement to make suit as string with their pairs that was decided in the writeup
if suit == 1:
    suitStr = 'Clubs'
elif suit == 2:
    suitStr = 'Diamonds'
elif suit == 3:
    suitStr = 'Hearts'
elif suit == 4:
    suitStr = 'Spades'

# write desired output to standard output
stdio.writeln(rankStr + ' of ' + suitStr)
