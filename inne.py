# def suma_cyfr(n):
#   return sum(int(digit) for digit in str(n))
# print(suma_cyfr(int(input())))


def silnia(n):
  if n == 0:
    return 1
  else:
    return n * silnia(n-1)
print(silnia(int(input())))