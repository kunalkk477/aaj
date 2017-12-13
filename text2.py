import random ,string

vowel='aeiou'
consonant='qwrtypsdfghjklzxcvbnm'
in1=[]
alpha=input("enter the numbes of alphabets you wantin the name")
for i in range(int(alpha)):
    num=input("enter 'v' for vowel,'c' for consonant,'l' for letter:  ")
    in1.append(num)

def text():
    name=""
    for i in in1:
        if i=='v':
            letter1= random.choice(vowel)
        elif i=='c':
            letter1= random.choice(consonant)
        elif i=='l':
            letter1=random.choice(string.ascii_lowercase)
        else:
            letter1=i
        name=name+letter1

    return(name)


numbers= input("enter the number of names you want: ")
for i in range(int(numbers)):
    print(text())
