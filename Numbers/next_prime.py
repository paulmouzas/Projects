from prime_factor import isPrime

def get_primes():
    number = 3
    while True:
        if isPrime(number):
            yield number
        number += 1
if __name__ == '__main__':

    gen = get_primes()

    user_input = raw_input("Press enter to see the next prime number.")
    while user_input != 'q':
        print next(gen)
        raw_input()
        