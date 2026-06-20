def is_armstrong_number(number):
    num = list(str(number))  # Convert to string first, then list
    a = len(num)  # Length of the number
    b = 0
    
    for i in num:
        b += int(i) ** a  # Convert string digit to int
    
    # Check AFTER the loop completes
    if b == number:
        return True
    else:
        return False