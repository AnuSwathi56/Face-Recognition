##import os 
import time

f=open("Database.txt", 'r')

text=f.readlines()

print('Enter the Password')
pwd1=input()
pwd=str(pwd1)
print(pwd)


while True :
 if pwd == "123":
    print('Password Correct')
    
    print("enter Leture name ")
    xxx= raw_input()
    x=str(xxx)
    print(x)
    print("enter student name ")
    yy= raw_input()
    y=str(yy)
    print(y)
    count=0
    for i in text: 
        if x in i:
          if y in i:
            m,n,p,q=i.split('\t')
            #print(q)
            q=int(p)
            if q >= 0:
                count=count+1


    print(count)
    f.close()
 else:
    print('Wrong Password')
    continue
