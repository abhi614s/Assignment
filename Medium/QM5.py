# You are developing a program that analyzes weather data. Write a Python function that takes a list of temperature readings for a specific location and determines the average temperature, highest temperature, and lowest temperature.
# Input
# temperature_readings = [25, 28, 21, 24, 27] Output:
# Average Temperature: 25.0
# Highest Temperature: 28
# Lowest Temperature: 21

A, B, C, D, E = map(int, input().split())

average_temperature = (A + B + C + D + E )/5
highest_temperature = max(A,B,C,D,E)
lowest_temperature = min(A,B,C,D,E)

print(f"Average Temperature: {average_temperature}")
print(f"Highest Temperature: {highest_temperature}")
print(f"Lowest Temperature: {lowest_temperature}")
