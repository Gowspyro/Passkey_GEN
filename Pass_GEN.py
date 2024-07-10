import random 
import pickle 

word=input("Enter a 4 letter word for your password:")
letters=[]
for i in word:
	letters.append(i)

symbols=["~","!","@","#","$","%","^","&","*","(",")","_","-","+","=",":",";","<",">","?","/"]
digits=["0","1","2","3","4","5","6","7","8","9"]
password=[]
passkey=""
# Now there will be 7 possibilities 
def rand_dig(a):
    dig_sym=[]
    for i in range(1000*a):
        random.shuffle(digits)
        random.shuffle(symbols)
    if a%2==0:
        # get 2 dig and 2 symbols 
        for i in range(2):
            dig_sym.append(digits[i])
            dig_sym.append(symbols[i])
    else:
        # 3 symbols and 1 dig 
        for i in range(3):
            dig_sym.append(symbols[i])
        dig_sym.append(digits[7])
    for i in range(6969*a):
        random.shuffle(dig_sym)
    return dig_sym    
a=random.randint(1,7)
flr=rand_dig(a)
password.append(letters[0])     #A
if a==1:
    # A-B-C-D-
    password.append(flr[1])     #-
    password.append(letters[1]) #B
    password.append(flr[2])     #-
    password.append(letters[2]) #C
    password.append(flr[3])     #-
    password.append(letters[3]) #D
    password.append(flr[0])     #-
if a==2:
    # A--B--CD
    password.append(flr[2])     #-
    password.append(flr[0])     #-
    password.append(letters[1]) #B
    password.append(flr[1])     #-
    password.append(flr[3])     #-
    password.append(letters[2]) #C
    password.append(letters[3]) #D
if a==3:
    # A-B--C-D
    password.append(flr[3])     #-
    password.append(letters[1]) #B
    password.append(flr[0])     #-
    password.append(flr[1])     #-
    password.append(letters[2]) #C
    password.append(flr[2])     #-
    password.append(letters[3]) #D
if a==4:
    # A--B-C-D
    password.append(flr[0])     #-
    password.append(flr[1])     #-
    password.append(letters[1]) #B
    password.append(flr[2])     #-
    password.append(letters[2]) #C
    password.append(flr[3])     #-
    password.append(letters[3]) #D
if a==5:
    # A--BC--D
    password.append(flr[1])     #-
    password.append(flr[2])     #-
    password.append(letters[1]) #B
    password.append(letters[2]) #C
    password.append(flr[3])     #-
    password.append(flr[0])     #-
    password.append(letters[3]) #D
if a==6:
    # AB----CD
    password.append(letters[1]) #B
    password.append(flr)        #----
    password.append(letters[2]) #C
    password.append(letters[3]) #D

if a==7:
    # AB--C-D-
    password.append(letters[1]) #B
    password.append(flr[2])     #-
    password.append(flr[3])     #-
    password.append(letters[2]) #C
    password.append(flr[0])     #-
    password.append(letters[3]) #D
    password.append(flr[1])     #-
#print(password) 
for i in password:
    passkey=passkey+i
print(passkey,"\n","a is ",a)
