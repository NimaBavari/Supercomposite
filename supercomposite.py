import math


def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(num) + 1), 6):
        if num % i == 0 or num % (i + 2) == 0:
            return False
    return True


def get_abundancy(n):
    counter = 0
    for i in range(1, n + 1):
        if n % i == 0:
            counter += 1
    return counter / n


def get_most_abundant(collection):
    abundancies = []
    for number in collection:
        abundancies.append(get_abundancy(number))
    return collection[abundancies.index(max(abundancies))]


def generate_primes(n):
    primes = [2]
    for i in range(3, n + 1, 2):
        if is_prime(i):
            primes.append(i)
    return primes


def build_largest_primorial_under(n):
    prod = 1
    for prime in generate_primes(int(math.sqrt(n))):
        prod *= prime
        if prod > n:
            prod /= prime
            break
    return int(prod)


def generate_super_composite(given_number, proximity):
    upper_bound = int((1 + proximity) * given_number)
    lower_bound = int((1 - proximity) * given_number)
    largest_primorial = build_largest_primorial_under(lower_bound)
    upper_multiple = int(math.floor(upper_bound / largest_primorial))
    lower_multiple = int(math.ceil(lower_bound / largest_primorial))
    try:
        most_abundant = get_most_abundant(
            range(lower_multiple, upper_multiple + 1))
        return largest_primorial * most_abundant
    except ValueError:
        return None

print(generate_super_composite(180000000000000, 0.3))
