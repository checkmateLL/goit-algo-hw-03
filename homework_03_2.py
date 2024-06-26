import random

def get_numbers_ticket(min, max, quantity):
    try:
        # Checking if all inputs are correct. Must be integer numbers.
        # In case it's a float - it'll be converted to integer.
        # In case it's a text - user will get a message that input is incorrect
        min = int(min)
        max = int(max)
        quantity = int(quantity)
        print(max)
    except ValueError:
        print("All inputs must be integer numbers")
        return []
    
        # Checking that all numbers correspond to our rules
        # Min no less than 1, no more than 1000 and quantity is possible within this range
    if max < min:
        print("Max number should be bigger than min number")
        return []
    elif quantity > (max - min + 1):
        print("Quantity must be less than max number")
        return []
    elif max > 1000:
        print("Max must be 1000 or less")
        return []
    elif min < 1:
        print("Min must be 1 or bigger")
        return []

    # Creating ticket numbers as a set and returning sorted set as a final result
    ticket_numbers = set(random.sample(range(min, max + 1), quantity))
    return sorted(ticket_numbers)
    
    
 # Example   
print(get_numbers_ticket(2, 170, 5))

