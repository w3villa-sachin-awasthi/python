# Write a program to check the strength of a password based on the following rules:
# At least 8 characters long.
# Contains at least one uppercase letter.
# Contains at least one lowercase letter.
# Contains at least one digit.
# Contains at least one special character (!@#$%^&*).
def check(val):
    if(len(val)<8):
        return False
    smallChar=0
    capitalChar=0
    digit=0
    sphecialChar=0
    for i in range(0,len(val)):
        if val[i]>='A' and val[i]<='Z':
            capitalChar+=1
        elif val[i]>='a' and val[i]<='z':
            smallChar+=1
        elif val[i]>='1' and val[i]<='9':
            digit+=1
        else:
            sphecialChar+=1
    if(capitalChar<1 or smallChar <1 or digit <1 or sphecialChar <1):
        return False
    else:
        return True
    

password=input("enter the password : ")
if check(password):
    print("entered password is strong")
else:
    print("entered password is not strong")