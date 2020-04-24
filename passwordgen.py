#program to generate password
import string as s
import random as r
l=int(input("ENTER THE LENGTH OF PASSWORD REQUIRED "))
u=int(input("ENTER MINIMUM NUMBER OF UPPER-CASE LETTERS REQUIRED"))
#password may have more than specified number of upper casre letters
n=int(input("ENTER NUMBER OF INTEGER DIGITS REQUIRED "))
c=int(input("ENTER NUMBER OF SPECIAL CHARACTERS REQUIRED "))
p=[]
char=['~','!','@','#','%','^','&','*','_','-']
a=l-u-n-c
if(a<0):
  print('PASSWORD WITH GIVEN VALUES CANT BE GENERATED')
  
#a is number of alphabets
else:
 for i in range(u):
   x=r.choice(s.ascii_uppercase)
   p.append(x)
 for i in range(n):
   x=r.randint(0,10)
   p.append(x)
 for i in range(c):
   x=r.randint(0,len(char))
   y=char[x]
   p.append(y)
 for i in range(a):
   x=r.choice(s.ascii_letters)
   p.append(x)
 print('\nGENERATED PASSWORD:"',end='')
 r.shuffle(p)
 for i in p:
   print(i,end='')
print('"\n')
