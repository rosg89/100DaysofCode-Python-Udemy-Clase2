#Data Types 

#String
print("This is a String: Hello")

#Subscripting
print("Hello"[0])

#Integer
#Whole numbers, without decimals
print(123)
print(2+2)
print(-1)

#Float
#Numbers with decimal places
print(3.05)

#Boolean
#True or False
print(True)

#Turn an Int into a String
num_char = len(input("What is your name?"))

new_num_char = str(num_char)

print("Your name has " + new_num_char + " characters.")

#Turn an Int into a String
a = str(123)
print(type(a))

#Turn an Int into a Float
a = float(123)
print(type(a))

#Turn a String into a Float
a = float("100.5")
print(type(a))
print(70 + a)

##################

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

#print(type(two_digit_number))
first_digit = two_digit_number[0]
second_digit = two_digit_number[1]

result = int(first_digit) + int(second_digit)

print(result)

########
#Mathematical Operations

# 3 + 5
# 3 - 5
# 3 * 5
# 3 / 5
# 3 ** 5

#PEMDAS - Left to Right
#Parentheses ()
#Exponents **
#Multiplication * and Division /
#Addition + and Substraction -

#Round
print(round(8/3, 2))

#Me retorna un INT
print(8//3)

