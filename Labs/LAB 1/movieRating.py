# Imported Moduals to help
import math
import re


# Sample Run
"""
Please enter the movie name.
CSC 155 The Movie!
Please enter the running time in minutes.
135
Please enter ratings from the movie review website.
75
99
10
Please enter ratings from the focus group.
84.5
92.3
Please enter the average movie critic rating.
87.58
Title: CSC 155 The Movie!
Running time: 2h15
Average website rating: 61.33
Average focus group rating: 88.40
Average movie critic rating: 87.58
Overall movie rating: 83
"""


# Getting the title
title = "Title: " + str(input("Please enter the movie name.\n"))


# Getting the runtime and converting it to hours
runTime = int(input("Please enter the running time in minutes.\n"))
runTimeHour = (
    "Running time: " + str(math.floor(runTime / 60)) + "h" + str((runTime % 60))
)


# Getting the website ratings and finding the average
websiteRatings = (
    float(input("Please enter ratings from the movie review webstite.\n"))
    + float(input())
    + float(input())
)
websiteRatingsAVG = "Average website rating: " + ("{:.2f}".format(websiteRatings / 3))


# Getting and focus group ratings and finding the average
focusGroupRatings = float(
    input("Please enter ratings from the focus group.\n")
) + float(input())
focusGroupRatingsAVG = "Average focus group rating: " + (
    "{:.2f}".format(focusGroupRatings / 2)
)

# Getting the critic average
criticRatings = float(input("Please enter the average movie critic rating.\n"))
criticRatingsAVG = "Average movie critic rating: " + str("{:.2f}".format(criticRatings))


# priniting out the averages before weighing
print(title)
print(runTimeHour)
print(websiteRatingsAVG)
print(focusGroupRatingsAVG)
print(criticRatingsAVG)


# Getting the numbers from the averages
criticRatingsAVG = re.findall("\d+\.?\d+", criticRatingsAVG)
websiteRatingsAVG = re.findall("\d+\.?\d+", websiteRatingsAVG)
focusGroupRatingsAVG = re.findall("\d+\.?\d+", focusGroupRatingsAVG)


# Weighing the averages
criticRatingsAVG = sum([float(i) for i in criticRatingsAVG]) * 0.50
websiteRatingsAVG = sum([float(i) for i in websiteRatingsAVG]) * 0.20
focusGroupRatingsAVG = sum([float(i) for i in focusGroupRatingsAVG]) * 0.30

# Finding and printing the rounded overall rating
overallRating = round(websiteRatingsAVG + focusGroupRatingsAVG + criticRatingsAVG)
print('Overall movie rating:', overallRating)