rc1 = input("please input c1: ")
rc2 = input("please input c2: ")

def tupalize_c(c1):
    (a1, b1) = [int(num) for num in c1.replace('i', "").split('+')]
    return (a1, b1)

def add_raw_cs(rc1, rc2) :
    (a1,b1) = c1.split('+')
    (a2,b2) = c2.split('+')
    a3 = str(int(a1) + int(a2))
    b3 = str(int(b1.replace('i', "")) + int(b2.replace('i', ""))) + "i"
    c3 = (a3, b3)
    return c3

def add_cs(c1, c2):
    (a1, b1) = c1
    (a2, b2) = c2
    a3 = a1 + a2
    b3 = b1 + b2
    return (a3, b3)

def subtract_cs(c1, c2):
    (a1, b1) = c1
    (a2, b2) = c2
    a3 = a1 - a2
    b3 = b1 - b2
    return  (a3, b3)

def multiply_cs(c1, c2):
    (a1, b1) = c1
    (a2, b2) = c2
    a3 = (a1 * a2 - b1 * b2)
    b3 = (a1 * b2 + a2 * b1)
    return (a3, b3)

def divide_cs(c1, c2):
    (a1, b1) = c1
    (a2, b2) = c2
    a3 = ((a1 * a2 + b1 * b2)/(a2 * a2 + b2 * b2))
    b3 = ((a2 * b1 - a1 * b2)/(a2 * a2 + b2 * b2))
    return (a3, b3)

def print_modulus(c1):
    (a1, b1) = c1
    result = (a1 * a1) + (b1 * b1)
    print("modulus of " + str(c1) + " : sqrt(" + str(result) + ")")

def complex_conjugate(c1):
    (a1, b1) = c1
    b1 = -b1
    return (a1, b1)

(a1, b1) = tupalize_c(rc1)
(a2, b2) = tupalize_c(rc2)
c1 = (a1, b1)
c2 = (a2, b2)

print((a1,b1))
print("addition of c1 and c2: " + str(add_cs(c1, c2)))
print("product of c1 and c2: " + str(multiply_cs(c1, c2)))
print("subtraction of c1 by c2: " + str(subtract_cs(c1, c2)))
print("division of c1 by c2: " + str(divide_cs(c1, c2)))
print_modulus(c1)
print_modulus(c2)
print("conjugate of c1: " + str(complex_conjugate(c1)))
print("conjugate of c2: " + str(complex_conjugate(c2)))

                                      


