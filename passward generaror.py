import string
import random
s=[]
s1=string.ascii_lowercase
s2=string.ascii_uppercase
s3=string.digits
s4=string.punctuation
#passlen=int(input('enter password length in positive integers: \n'))
s.extend(list((s1)))
s.extend(list((s2)))
s.extend(list((s3)))
s.extend(list((s4)))
#print(s)
random.shuffle(s)
#print(s)
check=True
while check==True:
    passlen = (input('enter password length in positive integers: \n'))
    if passlen.isdigit()==True:
        passlength=int(passlen)
        check=False
    else:
        print("Enter valid integer:")
        continue
passw=''.join(s)
print(passw[0:passlength])