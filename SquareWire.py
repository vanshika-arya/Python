radius = 42
angle_degrees = 60
pi = 22 / 7 

arc_length = 2 * pi * radius * (angle_degrees / 360)

side = arc_length / 4
area = side * side
print(int(area))