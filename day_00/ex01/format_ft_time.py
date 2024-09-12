from time import time
from datetime import date

# Get the current time
current_time = time()
print("Seconds since January 1, 1970:", f'{float(round(current_time, 4)):,}', "or", f'{current_time:n}', "in scientific notation")

# Get the current date
today = date.today()

# Textual month, day and year	
print(today.strftime("%b %d %Y"))