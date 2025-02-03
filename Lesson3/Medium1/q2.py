def factors(number):
    divisor = number
    result = []
    while divisor > 0:
#number % divisor == 0 is here to check to see if the number divided by the divisor is a factor, if not 0 is isn't
        if number % divisor == 0:
            result.append(number // divisor)     
        divisor -= 1
    return result


print(factors(-1))
print(factors(4))
