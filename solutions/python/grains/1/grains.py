def square(number):
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    
    # Square n has 2^(n-1) grains
    return 2 ** (number - 1)

def total():
    # Sum of all grains on all 64 squares
    # This is 2^64 - 1
    return 2 ** 64 - 1