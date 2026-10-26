
"""lab task 2"""
"""Weekend Temperature with a Tuple"""

times = ("morning", "noon", "night")

# Input Saturday temperatures
print("\nTEMPERATURE FOR SATURDAY-\n")
saturday_temp = []

for i in times:
    temp = float(input(f"Enter Saturday's temperature for {i}: "))
    saturday_temp.append(temp)

# Input Sunday temperatures
print("\nTEMPERATURE FOR SUNDAY-\n")
sunday_temp = []

for i in times:
    temp = float(input(f"Enter Sunday's temperature for {i}: "))
    sunday_temp.append(temp)

# Convert lists into tuples
saturday_temp = tuple(saturday_temp)
sunday_temp = tuple(sunday_temp)

# Display Saturday temperatures using a for loop
print("\nSaturday's temperatures:")
for i in range(len(times)):
    print(f"{times[i]}: {saturday_temp[i]}°C")

# Display Sunday temperatures using a for loop
print("\nSunday's temperatures:")
for i in range(len(times)):
    print(f"{times[i]}: {sunday_temp[i]}°C")

# Calculate highest and lowest temperatures
saturday_max_temp = max(saturday_temp)
saturday_min_temp = min(saturday_temp)

sunday_max_temp = max(sunday_temp)
sunday_min_temp = min(sunday_temp)

# Display results
print(f"\nHighest temperature on Saturday: {saturday_max_temp}°C")
print(f"Lowest temperature on Saturday: {saturday_min_temp}°C")

print(f"\nHighest temperature on Sunday: {sunday_max_temp}°C")
print(f"Lowest temperature on Sunday: {sunday_min_temp}°C")

# Highest and lowest temperatures for the whole weekend
weekend_temp = saturday_temp + sunday_temp

print(f"\nHighest temperature of the weekend: {max(weekend_temp)}°C")
print(f"Lowest temperature of the weekend: {min(weekend_temp)}°C")
