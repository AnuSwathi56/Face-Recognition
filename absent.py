##import os 
import time
import re

from twilio.rest import Client

# Find these values at https://twilio.com/user/account
account_sid = "AC5ccf64825986f8f34c6b42bfba0334d5"
auth_token = "2ebf9e425b210d4563e4e5f6f76bf368"

client = Client(account_sid, auth_token)


f=open("Database.txt", 'r')


f1=open("Database_new_ct.txt", 'a')
pj=0
sd=0
count =0
enter =0
text=f.readlines()
#while True:

text=str(text)       
print(text)

#if re.search( 'Prashanth', text ):
if 'Prashanth' not  in text:
    print('Prashanth ansent')
    pj=1
    f1.write("Prashanth"+'\t' +str('abs')+'\t'+'\n')
    print('send sms')
    client.api.account.messages.create(
    to="+91-9741607401",
    from_="+13344714713" ,  #+1 210-762-4855"
    body="Prashanth is Absent " )
if 'ujjwal'  not in text :
    print('ujjwal absent')
    pj=1
    f1.write("ujjwal"+'\t' +str('abs')+'\t'+'\n')
if 'bunty'  not in text :
    sd=1
    print('bunty Ansent')
    client.api.account.messages.create(
    to="+91-9741607401",
    from_="+13344714713" ,  #+1 210-762-4855"
    body="Bunty is Absent " )
    f1.write("bunty"+'\t' +str('absent')+'\t'+'\n')
    enter=1
            

##        if pj == 1 :
##            print('dfdf')
##            f1.write("prajwal"+'\t' +str('presrnt')+'\t'+'\n')
##        else:
##            f1.write("prajwal"+'\t' +str('absent')+'\t'+'\n')
##
##        if sd == 1 :
##            f1.write("syed"+'\t' +str('presrnt')+'\t'+'\n')
##        else:
##            f1.write("syed"+'\t' +str('absent')+'\t'+'\n')
        
f.close()
f1.close()

    
## if pwd == "123":
##    print('Password Correct')
##    
##    print("enter Leture name ")
##    xxx= raw_input()
##    x=str(xxx)
##    print(x)
##    print("enter student name ")
##    yy= raw_input()
##    y=str(yy)
##    print(y)
##    count=0
##    for i in text: 
##        if x in i:
##          if y in i:
##            m,n,p,q=i.split('\t')
##            #print(q)
##            q=int(p)
##            if q >= 0:
##                count=count+1
##
##
##    print(count)
##    f.close()
## else:
##    print('Wrong Password')
##    continue
