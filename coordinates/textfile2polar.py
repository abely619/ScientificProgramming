from coordinate_math import *

fp = open("cartesian_points.dat", "r")
points = parse_points(fp)
for i in range(len(points)):
    polar_points = cartesian_to_polar(points[i])
    print(polar_points)

io = open("polar_points.txt", 'w')

for i in range(len(polar_points)):
    printed_polar_points[i] = str(polar_points[i])
    print(printed_polar_points[i])
