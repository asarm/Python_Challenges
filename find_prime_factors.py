#Calculates all factors and checks if they are prime
def get_prime(number):
    factors = []
    i = 2
    while number != 1:
        if number % i == 0:
            number = number / i
            factors.append(i)
        else:
            i += 1
    return factors

num = int(input('Enter a number:'))
try:
    print(get_prime(num))
except:
    print('Invalid input')