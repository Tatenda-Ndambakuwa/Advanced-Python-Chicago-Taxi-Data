import os
import sys
import math 

for line in sys.stdin:
        entry = line.strip().split(",")
        
        # Pickup Centroid Latitude, Pickup Centroid Longitude, Dropoff Centroid Latitude and Dropoff Centroid Longitude
        pick_la, pick_lon, drop_la, drop_lon = entry[11],entry[12],entry[14],entry[15]
        
        # pick up community area
        area = entry[8]
        
        # calculate euclidean distance for each trip
        dist = math.sqrt((pick_la - drop_la)**2 + (pick_lon - drop_lon)**2)
        
        print('{}\t{}'.format(area,dist))