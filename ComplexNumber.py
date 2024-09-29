c1 = input("please input c1: ")
c2 = input("please input c2: ")

(a1,b1) = c1.split('+')
print(a1)
print(b1)

(a2,b2) = c2.split('+')

print(a2)
print(b2)

a3 = int(a1) + int(a2)

if b1.endswith('i') and b2.endswith('i') :
    b3 = (int(b1.replace('i', "")) + int(b2.replace('i', "")))
print("the product of c1 and c2 is: " + str(a3) + " + " + str(b3) + "i")

#print(str(eval(a1) + eval(a2)) + " + " + str(eval(b1) + eval(b2)) + "i")
