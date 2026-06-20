def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")

    aliquot_sum = 0

    for i in range(1, number):
        if number % i == 0:
            aliquot_sum += i

    if aliquot_sum == number:
        return "perfect"
    elif aliquot_sum > number:
        return "abundant"
    else:
        return "deficient"