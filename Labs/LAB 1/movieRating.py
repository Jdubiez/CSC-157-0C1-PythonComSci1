
import math
'''
Sample Run:
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
'''

movieTitle = 'Title: ' + str(input('Please enter the movie name.\n'))
print(movieTitle)

movieRunTime = int(input('Please enter the running time in minutes.\n'))

runTimeHour=  'Running time: '+ str(math.floor(movieRunTime/60)) + 'h' + str((movieRunTime%60))
print(runTimeHour)


movieReviewRatings =float(input
    ('Please enter ratings from the movie review webstite\n')) + float(input()) + float(input())

movieReviewRatingsAVG = print("{:.1f}".format(movieReviewRatings/3))



