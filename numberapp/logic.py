import math
import requests
from django.conf import settings 

def is_num_perfect(number):
    """Check if a number is perfect."""
    return sum(num for num in range(1, number // 2 + 1) if number % num == 0) == number


def is_num_prime(number):
    """Check if a number is a prime number."""
    if number < 2:
        return False
    for num in range(2, int(math.sqrt(number)) +1):
        if number % num == 0:
            return False
    return True

def return_num_properties(number):
    """Return properties of a given number (Armstrong, even, odd)."""

    properties = []

    # Armstrong number
    num_str = str(number)
    num = len(num_str)
    total = sum(int(digit) ** num for digit in num_str)

    if total == number:
        properties.append("armstrong")

    #check Odd or even number
    properties.append("even" if number % 2 == 0 else "odd")

    return properties

def sum_number_digit(number):
    """Sum all the digits of a number."""
    return sum(int(digit) for digit in str(number))

def get_funfact_for_number(number):
    """Retrieves funfacts of number using external api"""

    url = f"{settings.NUMBERAPI}/{number}/math"
    try:
        res = requests.get(url, timeout=5) # timeout to avoid long wait
        res.raise_for_status() #raise exception if status code 4xx/5xx
        return res.text
    except (requests.ConnectionError, requests.Timeout):
        return "No Internet connection, unable to fetch funfact"
    except requests.RequestException:
        return "Failed to retrieve funfact"


    



