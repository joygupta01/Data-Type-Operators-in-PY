Name = "Joy"
Age = 17
Weight = 50.5
is_student = True
print(type(Name))
print(type(Age))
print(type(Weight))
print(type(is_student))

print("After type casting")
Age = str(Age)
print(type(Age))

num1 = 5
num2 = 7
print("addition" ,num1+num2)
print("subtraction" ,num1-num2)
print("multiplication" ,num1*num2)
print("division" ,num1/num2)
print("float" ,num1//num2)
print("modulous" ,num1%num2)
print("exponents" ,num1**3)

print("equal" ,num1==num2)
print("not equal" ,num1!=num2)
print("greater" ,num1>num2)
print("lesser" ,num1<num2)


result = num1/2+num2**2+10
print(result)


first_name = "Codingal"
last_name = "student"
full_name = first_name+last_name

print(first_name)
print(last_name)
print(full_name)

word = "Gupta"
print(len(word))
print(word[0])
print(word[4])
print(word[0:3])


x = input("enter value of x")
y = input("enter value of y")

temp = x
x = y
y = temp

print("value of x after swapping" ,x)
print("value of y after swapping" ,y)
