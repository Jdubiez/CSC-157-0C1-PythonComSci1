# **************************************************************************
# * Name: Jahson Westby                                             CSC 157
# * Date: 9-28-23                                                     LAB 2
# *************************************************************************
# * Problem Statement and Specifications:
# * Ask user for details of plane then create plane with their details
# * then print the diffrence in planes (distance, direction, altitude)
# * Input:
# * callsign, distance, direction, altitude
# * Output:
# * initial positions:
# * (plane1): callsign, distance, direction, altitude
# * (plane2): callsign, distance, direction, altitude
# * distance between planes
# * height between planes
# * new positions:
# * (plane1): callsign, distance, direction, altitude
# * (plane2): callsign, distance, direction, altitude
# * distance between planes
# * height between planes
# *************************************************************************

from airplane import *
ap = Airplane

# create default airplane
p1 = Airplane()

# Get inputs for second plane
callsign = input(
    "Enter the details of the second airplane (call-sign, distance, bearing and altitude): "
).upper()
distance = float(input())
direction = int(input())
altitude = int(input())

# Create second plane
p2 = ap(callsign, distance, direction, altitude)

#C reate variables for distance and height difference
disBtw = "The distance between the planes is " + str(ap.distTo(p1, p2)) + " miles."
altBtw = (
    "The difference in height between the planes is "
    + str(abs(p1.altitude - p2.altitude))
    + " feet."
)

# Print initial positions
print(
    "Initial Positions: \n" '"Airplane 1":',
    ap.__str__(p1),
    '"Airplane 2":',
    ap.__str__(p2),
    "\n" + str(disBtw),
    "\n" + str(altBtw),
)

# Move planes 
for i in range(4):
    ap.gainAlt(p1)
    if i % 2 == 0:
        if p2.altitude < 2000:
            p2.altitude = 0
        else:
            p2.altitude -= 1000

p1.move(10.5, 50)
p2.move(8.0, 125)

# Update differance in distance and height variables
disBtw = "The distance between the planes is " + str(ap.distTo(p1, p2)) + " miles."
altBtw = (
    "The difference in height between the planes is "
    + str(abs(p1.altitude - p2.altitude))
    + " feet."
)

# Print new positions
print(
    "New Positions: \n" '"Airplane 1":',
    ap.__str__(p1),
    "\n" '"Airplane 2":',
    ap.__str__(p2),
    "\n" + str(disBtw),
    "\n" + str(altBtw),
)
