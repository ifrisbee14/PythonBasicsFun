# Isabella Frisbee
# CPSC 122
# Description: 

input_file = open("ny.ppm", "r")

magic_number = input_file.readline().strip()
dimensions = input_file.readline().strip()
width = int(dimensions[0])
height = int(dimensions[1])
max_color = int(input_file.readline().strip())

image = []
for row in range(639):
    row_pixels = []
    for col in range(width):
        r = int(input_file.readline())
        g = int(input_file.readline())
        b = int(input_file.readline())
        row_pixels.append([r, g, b])
    image.append(row_pixels)

for row in range(height):
    for col in range(width):
        image[row][col][0] = 0

input_file.close