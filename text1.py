import random ,string

vowel='aeiou'
consonant='qwrtypsdfghjklzxcvbnm'

in1=input("enter v for vowel,c for consonant,l for letter:  ")
in2=input("enter v for vowel,c for consonant,l for letter:  ")
in3=input("enter v for vowel,c for consonant,l for letter:  ")

def text():
    if in1=='v':
        letter1= random.choice(vowel)
    elif in1=='c':
        letter1= random.choice(consonant)
    elif in1=='l':
        letter1=random.choice(string.ascii_lowercase)
    else:
        letter1=in1

    if in2=='v':
        letter2= random.choice(vowel)
    elif in2=='c':
        letter2= random.choice(consonant)
    elif in2=='l':
        letter2=random.choice(string.ascii_lowercase)
    else:
        letter2=in1

    if in3=='v':
        letter3= random.choice(vowel)
    elif in3=='c':
        letter3= random.choice(consonant)
    elif in3=='l':
        letter3=random.choice(string.ascii_lowercase)
    else:
        letter3=in3

    name= letter1+letter2+letter3
    return(name)


numbers= input("enter the number of names you want: ")
for i in range(int(numbers)):
    print(text())
