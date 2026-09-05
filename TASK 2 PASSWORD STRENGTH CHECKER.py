#SUBMITTED BY CHAHNA GUPTA, BCA 1-C
print("SUBMITTED BY \t CHAHNA GUPTA")
print("BCA 1-C")
print("PASSWORD STRENGTH CHECKER")

password = input("ENTER PASSWORD:")
score = 0
uppercase = False
lowercase = False
number = False
special = False

for x in password:
    if x>="A" and x<="Z":
        uppercase = True
    if x>="a" and x<="z":
        lowercase = True
    if x in "0123456789":
        number = True
    if x=="!" or x=="@" or x=="#" or x=="$" or x=="%" or x=="&" or x=="*" or x=="^" or x=="-" or x=="+" or x=="_"or x=="~" or x=="`" or x=="(" or x==")" or x=="=" or x=="[" or x=="]" or x=="{" or x=="}" or x==":" or x==";"or x=="'" or x=="," or x=="<" or x==">" or x=="?" or x=="/" or x==".":
        special = True
print ("_________________________________________________________________________________")
print ("PASSWORD ANALYSIS")
#LENGTH
if len(password)>=8:
    print("Atleast 8 characters: YES")
    score = score + 1
else:
    print("Atleast 8 characters: NO")
#UPPERCASE
if uppercase:
    print("Contains uppercase: YES")
    score = score + 1
else:
    print("Contains uppercase: NO")
#LOWERCASE
if lowercase:
    print("Contains lowercase: YES")
    score = score + 1
else:
    print("Contains lowercase: NO")
#SPECIAL
if special:
    print("Conatins special characters: YES")
    score = score + 1
else:
    print("Contains special character: NO")
#NUMBER
if number:
    print("Contains a number: Yes")
    score = score + 1
else:
    print("Contains a number: NO")
print ("_________________________________________________________________________________")                
#CHECKING PASSWORD STRENGTH
print("ANALYSING YOUR PASSWORD STRENGTH")

if score<=2:
    print("PASSWORD STRENGTH: WEAK")
elif score<=4:
    print("PASSWORD STENGTH: MEDIUM")
else:
    print("PASSWORD STENGTH: STRONG")
print ("_________________________________________________________________________________")
        
print("BY \t CHAHNA GUPTA")
print("BCA 1-C")
# BY CHAHNA GUPTA, BCA 1-C 
