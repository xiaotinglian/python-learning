a = 12
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a / b)  # 4.0
print(a // b)  # 4 integer division,
print(a % b)  # remainder.

print()

for i in range(1, a//b):  # (1, a/b)is not allowed since a/b is float.
    print(i)

print(a + b / 3 - 4 * 12)