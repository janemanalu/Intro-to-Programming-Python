import math
import stdio
import sys
from blob_finder import BlobFinder
from picture import Picture


# Entry point
def main():
    # accept pixels (int), tau (float), delta(float), frames (list) as command line arguments
    pixels = int(sys.argv[1])
    tau = float(sys.argv[2])
    delta = float(sys.argv[3])
    frames = sys.argv[4:]

    # Construct a BlobFinder object for the frame sys.argv[4] and from it get a list of beads prevBeads that have at
    # least pixels pixels.
    bf = BlobFinder(Picture(frames[0]), tau)
    prevBeads = bf.getBeads(pixels)


    for i in range(1, len(frames)):
        # Construct a BlobFinder object and from it get a list of beads currBeads that have at least pixels pixels.
        bf = BlobFinder(Picture(frames[i]), tau)
        currBeads = bf.getBeads(pixels)

        #For each bead currBead in currBeads, find a bead prevBead from prevBeads that is no further than delta and is
        # closest to currBead, and if such a bead is found, write its distance (using format string ’%.4f\n’) to
        # currBead
        for currBead in currBeads:
            closest = math.inf
            for prevBead in prevBeads:
                r = currBead.distanceTo(prevBead)
                if r <= delta and r < closest:
                    closest = r
            if closest != math.inf:
                stdio.writef('%.4f\n', closest)

        # Write a newline character.
        stdio.writeln()

        # Set prevBeads to currBeads.
        prevBeads = currBeads



if __name__ == '__main__':
    main()
