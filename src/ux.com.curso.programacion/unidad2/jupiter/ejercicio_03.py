#If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace in seconds per mile?

#First, we need to convert the total time into seconds.
minutes = 42
seconds = 42
total_seconds = (minutes * 60) + seconds

#Next, we need to convert the distance from kilometers to miles. We know that there are 1.61 kilometers in a mile.
kilometers = 10
miles = kilometers / 1.61

#Finally, we can calculate the average pace in seconds per mile by dividing the total time in seconds by the distance in miles.
average_pace = total_seconds / miles
print("Your average pace is", average_pace, "seconds per mile.")

#What is your average pace in minutes and seconds per mile?
#To convert the average pace from seconds per mile to minutes and seconds per mile, we can use the divmod function to get the quotient and remainder when dividing the average pace by 60.
minutes_per_mile, seconds_per_mile = divmod(average_pace, 60)
print("Your average pace is", int(minutes_per_mile), "minutes and", int(seconds_per_mile), "seconds per mile.")

#What is your average speed in miles per hour?
#To calculate the average speed in miles per hour, 
# we can divide the distance in miles by the total time in hours. 
# We can convert the total time from seconds to hours by dividing it by 3600.
total_hours = total_seconds / 3600
average_speed = miles / total_hours
print("Your average speed is", average_speed, "miles per hour.")