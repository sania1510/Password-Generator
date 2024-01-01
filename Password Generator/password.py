import string
import random

string1=string.ascii_uppercase
string2=string.ascii_lowercase
string3=string.digits
string4=string.punctuation
    
password_length=int(input("enter the value of the length of the password : "))
print()
final_string=[]
final_string.extend(list(string1))
final_string.extend(list(string2))
final_string.extend(list(string3))
final_string.extend(list(string4))

random.shuffle(final_string)
print("Your password is : ")
print("".join(final_string[0:password_length]))
print()