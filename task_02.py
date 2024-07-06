import random

def get_muber_tickets (min, max, quantity):
    if min < 1 or max > 1000 or quantity < 1 or quantity > (max - min +1):
        return[]
    
    numbers = random.sample(range(min, max, +1), quantity)
    return sorted(numbers)

lottery_numbers = get_muber_tickets (1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)