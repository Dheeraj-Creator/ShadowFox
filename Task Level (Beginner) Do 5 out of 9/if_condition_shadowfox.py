#4. If Condition

#BMI Category Determination

height=float(input("Enter height in meters: "))
weight=float(input("Enter weight in kilograms: "))
bmi=weight/(height**2)
if bmi>=30:
    print("obesity")
elif 25<=bmi<30:
    print("overweight")
elif 18.5<=bmi<25:
    print("normal")
else:
    print("underweight")

#Determine the country of a city

australia=["Sydney","Melbourne","Brisbane","Perth"]
uae=["Dubai","Abu Dhabi","Sharjah","Ajman"]
india=["Mumbai","Bangalore","Chennai","Delhi"]

city=input("enter a city name: ")
if city in australia:
    print(f"{city} is in Australia")
elif city in uae:
    print(f"{city} is in UAE")
elif city in india:
    print(f"{city} is in India")
else:
    print(f"{city} is not in the list")

#Check if two cities belong to the same country

city1=input("Enter the first city: ")
city2=input("Enter the second city: ")

if city1 in australia and city2 in australia:
    print("Both cities are in Australia")
elif city1 in uae and city2 in uae:
    print("Both cities are in UAE")
elif city1 in india and city2 in india:
    print("Both cities are in India")
else:
    print("They don't belong to the same country")


