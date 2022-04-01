import math
# Arithmetic Operators
# Addition:         3 + 2
# Subtraction:      3 - 2
# Multiplication:   3 * 2
# Division:          3 / 2
# Floor Division:    3 // 2 gives the nearest integer which is not greater than the result
# Exponent:         3 ** 2
# Modulus:          3 % 2
# divmod(x, y)      divmod(4, 2)

print(abs(-8))      # Prints 8
print(round(3.75))  # Prints 4
print(round(3.75, 1))   # Prints 3.8
print(divmod(4, 2))     # Returns (x // y, x % y)

p = 3.9
print(round(p))     # Prints 4
print(math.trunc(p))    # Prints 3  uses __trunc__ magic method

# formatting numbers

x = 1.2345
print(format(x, '0.2f'))    # Prints 1.23
print(format(x, '0.3f'))    # Prints 1.234

# Comparision operators
# Equal:            3 == 2
# Not Equal:        3 != 2
# Greater Than:     3 > 2
# Less Than:        3 < 2
# Greater or Equal: 3 >= 2
# Less or Equal:    3 <= 2

# The above comparisions return booleans

num1 = 3
num2 = 2
print(num1 + num2)  # Prints 5

num1 = '3'
num2 = '2'
print(num1 + num2)  # Prints 32

# Casting String to Integer
print(int(num1) + int(num2))    # Prints 5
