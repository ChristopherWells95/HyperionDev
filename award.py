# Swimming, running and cycling variables will store the times of the athletes in minutes and as a float.
swimming = float(input("Enter the time for swimming, in minutes: "))

running = float(input("Enter the time for running, in minutes: "))

cycling = float(input("Enter the time for cycling, in minutes: "))

# Total time will store the sum of the three disciplines.
total_time = cycling + running + swimming

# If an athlete finished in more than 0 but less than 100 minutes.
if total_time > 0 and total_time <= 100:
    print("Provincial colours.")
# Elif an athlete finished in 101 or more but less than 105 minutes.
elif total_time >= 101 and total_time <= 105:
    print("Provincial half colours.")

# Elif an athlete finished in 106 or more but less than 110 minutes.
elif total_time >= 106 and total_time <= 110:
    print("Provincial scroll.")

# if an athlete has more than 110 minutes, or did not finish.
else:
    print("No award.")