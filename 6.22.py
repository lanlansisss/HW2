# ERIC WANG
''' Read in first equation, ax + by = c '''
a = int(input())
b = int(input())
c = int(input())


''' Read in second equation, dx + ey = f '''
d = int(input())
e = int(input())
f = int(input())


check_solution = False
# loop
for x in range(-10, 10, 1):
    for y in range(-10, 10, 1):

        if a * x + b * y == c and d * x + e * y == f:
            check_solution = True

            print("{} {}".format(x,y))


if check_solution == False:
    print('No solution')