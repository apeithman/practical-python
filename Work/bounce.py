# bounce.py
#
# Exercise 1.5
height = 100
bounce_factor = 3/5
bounce_number = 1
while bounce_number < 11:
    height = bounce_factor * height
    print(bounce_number, round(height, 4))
    bounce_number += 1
