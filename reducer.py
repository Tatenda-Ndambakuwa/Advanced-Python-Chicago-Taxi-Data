import os
import sys

current_area = None
current_dist = 0.0
area = None
dist = 0.0

# number of trips in this area
num_trips = 0

for line in sys.stdin:
    area, dist = line.split('\t', 1)
            
    # convert distance (currently a string) to int
    try:
        dist = float(dist)
    except ValueError:
        # dist was not a number, so silently
        # ignore/discard this line
        continue

    # Since Hadoop sorts map output by key (here: area) before it is passed to the reducer
    if current_area == area:
        current_dist += dist
        num_trips += 1
    else:
        if current_area and i != 0:
            # write result to STDOUT
            print('{}\t{}'.format(current_area, current_dist/num_trips))
        current_area = area
        current_dist = dist
        num_trips = 0

# Output the last area if needed
if current_area == area and num_trips !=0:
    print('{}\t{}'.format(current_area, current_dist/num_trips))