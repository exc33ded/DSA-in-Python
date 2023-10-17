# Gicen the first two terms of an AP. Find the nth term.

n1 = float(input())
n2 = float(input())

diff = n2 - n1

n = int(input("Enter nth term to find"))
a_n_th = n1 + (n-1)*diff

print(f"The {n}th term is {a_n_th}")