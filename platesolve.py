import babeldix

import sys
import operator

# Print solutions in order of increasing score

for plate in sys.argv[1:]:
    solns = babeldix.Plates.get_solutions(plate)
    for (soln,score) in sorted(solns.items(), key=operator.itemgetter(1)):
        print '{0:s} {1:d} {2:s}'.format(plate,score,soln)
