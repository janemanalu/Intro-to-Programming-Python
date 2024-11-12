import stdarray
import stdrandom
import stdio

# receive the data for minuet measures from standard input(data/mozart.txt)
minuet_measures = stdarray.create2D(11, 16)
for i in range(11):
    for j in range(16):
        minuet_measures[i][j] = stdio.readInt()

# receive the data for trio measures from standard input(data/mozart.txt)
trio_measures = stdarray.create2D(6, 16)
for i in range(6):
    for j in range(16):
        trio_measures[i][j] = stdio.readInt()

# choosing a random value of minuet measures for each of the 16 columns, which are compiled to a new list(seq_minuet),
# using stdrandom as the fair die twice and then sum it for the row value.
seq_minuet = stdarray.create1D(16)
for a in range(16):
    value_row_dice1 = stdrandom.uniformInt(1, 7)
    value_row_dice2 = stdrandom.uniformInt( 1, 7)
    seq_minuet[a] = minuet_measures[value_row_dice1 + value_row_dice2 - 2][a]
    # write to standard output of the sequence of 16 minuet measures in one line separated with a space
    stdio.write(str(seq_minuet[a]) + ' ')

# choosing a random value of trio measures for each of the 16 columns, compiled to anew list(seq_trio), using stdrandom
# as the fair die once for the row value
seq_trio = stdarray.create1D(16)
for b in range(16):
    value_row_dice = stdrandom.uniformInt(1, 7)
    seq_trio[b] = trio_measures[value_row_dice - 1][b]
    # write to standard output of the sequence of 16 trio measure on the same line as the seq_minuet,
    # separated with a space
    stdio.write(str(seq_trio[b]) + ' ')

stdio.writeln()
