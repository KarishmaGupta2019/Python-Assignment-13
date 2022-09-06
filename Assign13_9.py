'''Write a Python script to create a list of city names taken from the user.'''

s1=input("Enter some cities followed by comma")
l1= [city for city in s1.split(',')]
print(l1)



