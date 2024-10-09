#Mehra_Rahul 201722843   October2023 CA-02.py


import math
#input
angle_in_deg = float(input("Enter the angle between 0 and 90 inclusive in degrees: "))
time = float(input("Enter the total time spent travelling in seconds: "))

#Proccess and calculations
angle_in_rad = math.radians(angle_in_deg)
speed = 1.5
battery_usage = 2.7
distance_travelled = (speed*time)
sina = math.sin(angle_in_rad)
cosa = math.cos(angle_in_rad)
horizontal_distance = (sina*distance_travelled)
vertical_distance = (cosa*distance_travelled)
battery_used = (battery_usage*time)
battery_remaining = (100-battery_used)
maximum_time = (100/2.7)
maximum_distance = (maximum_time*speed)


#output
print ("Angle used:",angle_in_deg,"degrees")
print ("Time of travel:",time,"s")
print (f"Distance travelled: {distance_travelled:.2f}","m")
print (f"Horizontal movement: {horizontal_distance:.2f}","m")
print (f"Vertical movement: {vertical_distance:.2f}","m")
if (distance_travelled > maximum_distance):
    print("Battery Usage: 100%")
    print("Battery remaining: 0%")
    print(f"Destination not reached,the rover has run out of battery after travelling {maximum_distance:.2f}","m")
elif(battery_used > battery_remaining):
    print ("Battery usage:",battery_used,"%")
    print ("Battery remaining:",battery_remaining,"%")
    print ("Destination reached however, battery levels are insufficient to return to base.")
else:
    print ("Battery usage:",battery_used,"%")
    print ("Battery remaining:",battery_remaining,"%")
    print ("Destination reached.Battery levels are sufficient to return to base.")
    



       
