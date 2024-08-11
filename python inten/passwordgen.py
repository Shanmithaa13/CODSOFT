import random

alphabets = [ 'a','b','c','d','e','f','g','h','i','j','k','l','m',
             'n','o','p','q','r','s','t','u','v','w','x','y','z']
num = ['1','2','3','4','5','6','7','8','9','0']
sign = ['!','@','#','$','%','^','&','*','(',')','_','+','*','/']
print("Welcome to Password Generator!")
length = int(input("Enter the length of the password: "))
n_alb = int(input("How many letters you want in your password?: \n"))
n_num = int(input("How many numbers you want in your password?: \n"))
n_sign = int(input("How many symbols you want in your password?: \n"))

password_list = []
for i in range (1,n_alb+1):
    char = random.choice(alphabets)
    password_list += char

for i in range (1,n_num+1):
    char= random.choice(num)
    password_list += char

for i in range (1,n_sign+1):
    char = random.choice(sign)
    password_list += char
print("Before shuffle:", password_list)

random.shuffle(password_list)

print("After shuffle: ",password_list)

password = ""
for chaa in password_list:
    password += chaa
print("The password you want: ",password)
