import math

@profile
def check_prime(number):
    sqrt_number = math.sqrt(number)
    number_float = float(number)
    for i in range(2,int(sqrt_number) + 1):
        if (number_float / i).is_integer():
            return False
    return True

print("check_prime(10000000) = ", check_prime(10000000))
print("check_prime(10000019) = ", check_prime(10000019))
