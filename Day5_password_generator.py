import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','#',"$",'%',"&",'(',')','*','+']

print("/*******************************************Welcome to the password Generator*************************************************")
n_letters=int(input("enter the number of letter you want"))
n_symbols=int(input("enter the number of symbols you want"))
n_numbers=int(input("enter the number of numbers you want"))
password=[]
for i in range(n_letters):
    password.append(letters[random.randint(0,len(letters)-1)])
for i in range(n_symbols):
    choice_index=random.randint(0,len(password)-1)
    password.insert(choice_index,symbols[random.randint(0,len(symbols)-1)])
for i in range(n_numbers):
    choice=random.randint(0,len(password)-1)
    password.insert(choice,numbers[random.randint(0,len(numbers)-1)])
final=""
for i in password:
    final+=i

print("Your Password is here ",final)

     