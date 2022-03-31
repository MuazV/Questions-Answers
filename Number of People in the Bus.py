"""There is a bus moving in the city, and it takes and drop some people
in each bus stop.

You are provided with a list (or array) of integer pairs. Elements of each
pair represent number of people get into bus (The first item) and number of
people get off the bus (The second item) in a bus stop.

Your task is to return number of people who are still in the bus after the
last bus station (after the last array). Even though it is the last bus stop,
the bus is not empty and some people are still in the bus, and they are probably
sleeping there :D

Take a look on the test cases.

Please keep in mind that the test cases ensure that the number of people in the bus
is always >= 0. So the return integer can't be negative.

The second value in the first integer array is 0, since the bus is empty in the first
bus stop."""

bus_stops = [[2, 0], [3, 4], [6, 3], [2, 5]]


def number(bus_stops):
    total = 0
    for i in range(len(bus_stops)):
        for j in range(len(bus_stops[i])):
            if j % 2 == 0:
                total += bus_stops[i][j]
            else:
                total -= bus_stops[i][j]
    return total

print(number(bus_stops))

# def number(bus_stops):
#     return sum([stop[0] - stop[1] for stop in bus_stops])