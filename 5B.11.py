def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

a = int(input())
b = int(input())
print(f"Greatest common divisor of {a} and {b} is {gcd(a,b)}")
