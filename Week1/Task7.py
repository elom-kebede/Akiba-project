destination = input("Enter the destination: ")
distance = float(input("Enter the distance in kilometers: "))
speed = float(input("Enter the speed in km/h: "))
time = distance / speed
time_in_min = time * 60
print(f"Destination: {destination}")
print(f"Distance: {distance} km")
print(f"Average speed: {speed} km/h")
print()
print(f"Estimated Travel Time in hours: {time} hours")
print(f"Estimated Travel Time in minutes: {time_in_min} minutes")


