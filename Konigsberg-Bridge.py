# Yogesh Naresh
# Bridges are denoted as lowercase letters
# Land masses are denoted as uppercase letters

from itertools import chain

#LANDbridgeLAND
BRIDGES = [
    "AaB",
    "AbB",
    "AcC",
    "AdC",
    "AeD",
    "BfD",
    "CgD"
]

def get_walks_starting_from(area, bridges = BRIDGES):
    walks = []

    # Recursive function that creates the walk, which is a String
    def make_walks(area, walked=None, bridges_crossed=None):
        # Either define walked as all the areas we've walked or start from area
        walked = walked or area

        # Tuple for all the bridges crossed
        bridges_crossed = bridges_crossed or ()

        # Getting all the bridges connected to present area that haven't been crossed
        avalable_bridges = []

        for bridge in bridges:
            if area in bridge and bridge not in bridges_crossed:
                # adding to available bridges only if the bridge has the area in the string and the
                # bridge is not crossed yet.
                avalable_bridges.append(bridge)

        # Checking if the walk is done
        if not avalable_bridges:
            # adding the bridges walked to the array of possible walks
            walks.append(walked)

        # Walking to an adjacent bridge
        for bridge in avalable_bridges:
            crossing = ''
            if bridge[0] == area:
                crossing = bridge[1:]
            else:
                crossing = bridge[1::-1]

            # Recursive Call
            make_walks(
                area = crossing[-1], # last char in the crossing string because that is where we end up
                walked = walked + crossing, # bridges walked plus the most recent crossing
                bridges_crossed = (bridge, *bridges_crossed) # updating tuple by adding current bridge at the start
                # and unpacking all the present bridges after the current bridge crossed
            )

    make_walks(area)
    return walks

# Generating a dictionary with the area and all the possible walks as the value
walks_starting_from = {}
for area in "ABCD":
    walks_starting_from[area] = get_walks_starting_from(area)

total_walks = 0
for walks in walks_starting_from.values():
    total_walks = total_walks + len(walks)

print(total_walks)

all_walks = chain.from_iterable(walks_starting_from.values())

solutions = []
for walk in all_walks:
    if len(walk) == 15:
        solutions.append(walk)

print(solutions) # no solutions
