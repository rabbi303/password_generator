
import random

numbers=['1','2','3','4','5','6','7','8','9']
special_char=['!','@','#','$','%','&','*','(','{','[',']']
char=['a','s','d','f','g','h','j','k','l','m','n','b','v','c','x','z','q','w','e','r','t','y','u','i','o','p','A','S','D','F','G','H','J','K','L','M','N','B','V','C','X','Z','Q','W','E','R','T','Y','U','I','O','P']



numbers_n=int(input('How many numbers you want in your Passward :'))
special_char_n=int(input('How many special character you want in your Passward :'))
char_n=int(input('How many latter you want in your Passward :'))

our_pass=[]

for nm in range(1,numbers_n+1):
    our_pass+=random.choice(numbers)

for sp in range(1,special_char_n+1):
    our_pass+=random.choice(special_char)

for cr in range(1,char_n+1):
    our_pass+=random.choice(char)

random.shuffle(our_pass)
passward=" "

for op in our_pass:
    passward += op
print('The strong passward is: ',passward)





