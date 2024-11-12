import math
import stdio


# Entry point.
def main():
    # Initialize ETA, RHO, T, and R to appropriate values
    ETA = 9.135e-4
    RHO = 5e-7
    T = 297.0
    R = 8.31457
    METERS_PER_PIXEL = 1.75e-7

    # accept the displacements of beads (output bead_tracker.py) from standard input, and compute their variance.
    displacements = stdio.readAllFloats()
    var = sum(map(lambda r: (METERS_PER_PIXEL * r) ** 2, displacements)) / (2 * len(displacements))

    # Compute Boltzmann and AVogadro constants, and write them to standard output.
    BOLTZMANN = 6 * math.pi * var * ETA * RHO / T
    AVOGADRO = R / BOLTZMANN
    stdio.writef('%e %e\n', BOLTZMANN, AVOGADRO)

if __name__ == '__main__':
    main()
