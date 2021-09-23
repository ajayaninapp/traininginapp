
import random
from random import randrange
threshold=5
class Pet:
    def __init__(self,name,sounds=[]) :
        self.name=name
        self.sounds=sounds
        self.hunger=randrange(6)
        self.boredom=randrange(6)


    def clock_tick(self):
        self.hunger=self.hunger+1
        self.boredom=self.boredom+1

    def __str__(self):
        if self.hunger>threshold and self.boredom>threshold:
            return f'\n{self.name} is hungry and bored'
        elif  self.hunger>threshold:
            return f'\n{self.name} is hungry'
        elif  self.boredom>threshold:
            return f'\n{self.name} is Bored'
        else:
            return f'\n{self.name} is happy'
    
    def reduce_boredom(self,bore):
        self.bore=bore
        self.boredom=self.boredom-self.bore
        if self.boredom<0:
            self.boredom=0


    def reduce_hunger(self):
        self.hunger=self.hunger-2


    def teach(self,word):
        self.word=word
        self.sounds.append(self.word)
        self.reduce_boredom(2)
        

    def hi(self):
        try:
            print(random.choice(self.sounds))
            self.reduce_boredom(1)
        except:
            print("I dont know any words")

    def feed(self):
        self.reduce_hunger()



def petselector(x):
    petname=''
    if x==2:
        petname='Jimmy'
        return petname
    elif x==1:
        petname='Tommy'
        return petname
    elif x==3:
        petname=input("Enter new petname\n")
        return petname
    else:
        print("invalid input")

        
        

x=int(input("select your pet :\n 1--Tommy\n2--Jimmy\n3--New adoption\n"))

name=petselector(x)

mypet=Pet(name)

print(mypet.hunger)

print(f'pet name:{mypet.name}\nhunger:{mypet.hunger}\nboredom:{mypet.boredom}\nwords:{mypet.sounds}')

something = False
while not something:
   

    a=int(input("commands available\n1---feed\n2---teach\n3---greet"))
    mypet.clock_tick()
    if a==1:
        mypet.feed()  

    elif a==2:
        word=input("enter word to teach:")
        mypet.teach(word)
    elif a==3:
        mypet.hi()
    else:
        print('invalid input')

    inout = input('type "y" to continue: ')
    if inout != 'y':
        something = True

print(f'pet name:{mypet.name}\nhunger:{mypet.hunger}\nboredom:{mypet.boredom}\nwords:{mypet.sounds}')

print(mypet)

   