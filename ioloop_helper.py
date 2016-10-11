import vote_tracker
import util
import live_config

fcns = (
    ['periodic_prune', vote_tracker.periodic_prune, 0],
)

def tick():
    for entry in fcns:
        entry[2] += 1
        if entry[2] >= live_config.d[entry[0]]:
            entry[2] = 0
            entry[1]()
