
import math

movieTitle = 'Title: ' + str(input('Please enter the movie name.\n'))
print(movieTitle)

movieRunTime = int(input('Please enter the running time in minutes.\n'))

runTimeHour=  'Running time: '+ str(math.floor(movieRunTime/60)) + 'h' + str((movieRunTime%60))
print(runTimeHour)


movieReviewRatings =float(input
    ('Please enter ratings from the movie review webstite\n')) + float(input()) + float(input())

movieReviewRatingsAVG = print("{:.1f}".format(movieReviewRatings/3))

