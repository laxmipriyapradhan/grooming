# String, ints, floats, strings and tuples are im-mutable objects
name = 'hello'
name[0] = 'y'   # Assignment not possible

nums = [1, 2, 3, 4, 5]
nums[0] = 100   # Assignment possible

my_tuple = (1, 2, ['a', 'b', 'c'], 3)
my_tuple[0] = 10    # Assignment not possible
my_tuple[2][0] = 'x'    # Assignemnt possible

name = 'a'
print(name)
print(f'Memory Address of {name} is {id(name)}')

name = 'b'      # A new String gets returned when the name variable is re-assigned with value 'b'
print(name)
print(f'Memory Address of {name} is {id(name)}')

other_name = name

name = 'c'
print(name)
print(other_name)   # other_name still holds the value 'b' even though name variable is changed to 'c'
# ====================================================

# Lists are Mutable Objects
names = ['apple', 'yahoo', 'google']
print(names)
print(f'Memory Address of {names} is {id(names)}')

# ASSIGNEMNT NEVER COPIES DATA
other_names = names     # Both names and other_names are pointing to the same memory location or Object
print(f'Memory Address of {other_names} is {id(other_names)}')

# Mutating the list
names[0] = 'instagram'  # Modify the original List 'names'
names.append('watsapp')
names.extend(['flipkart', 'netflix'])
names += ['samsung']    # Not sames as names = names + ['samsung']
# Internally it is extending the list by implementing __iadd__() method
print(other_names)      # 'other_names' will also get the modified copy of 'names'

# Re-binding (returns a new list)
names = names + ['microsoft']

# ====================================================
