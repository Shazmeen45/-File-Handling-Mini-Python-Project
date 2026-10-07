import random
import math
from datetime import datetime

# Random library
# This generates a random number between 1 and 100.
random_number = random.randint(1, 100)
print("Random number: ", random_number)

# Math library
# This calculates the square root of a number.
number = float(input("Enter a number: "))

if number >= 0:
    square_root = math.sqrt(number)
    print("Square Root of", number, "is:", square_root)
else:
    print("Square root cannot be calculated for a negative number.")

# Datetime library
current_datetime = datetime.now()
print("Current date and time is: ", current_datetime)