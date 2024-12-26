def right_triangle(a, b, c):
    s = sorted([a, b, c])
    return s[0]**2 + s[1]**2 == s[2]**2

a = int(input("Enter first side: "))
b = int(input("Enter  second side: "))
c = int(input("Enter side: "))


if right_triangle(a, b, c):
    print("The triangle is a right triangle.")
else:
    print("The triangle is not a right triangle.")
