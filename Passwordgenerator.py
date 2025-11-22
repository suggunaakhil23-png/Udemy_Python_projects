import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
chars = ['{','}','[',']','(',')','*','&','^','%','$','#','@','!']
numbers = ['1','2','3','4','5','6','7','8','9','0']

a = int(input("Enter the number of alphabets: "))
b = int(input("Enter the number of characters: "))
c = int(input("Enter the number of numbers: "))

password = []

for _ in range(a):
    password.append(random.choice(letters))

for _ in range(b):
    password.append(random.choice(chars))

for _ in range(c):
    password.append(random.choice(numbers))


random.shuffle(password)

final_password = "".join(password)
print("Your password is:", final_password)
