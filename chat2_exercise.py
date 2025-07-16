import re
import time


pets = ['dog', 'cat']
class Petowner:
    def __init__(self, pets):
        self.pets = pets
    @classmethod
    def addpet(cls):
        species = input('is it a dog or a cat ')
        while species not in ['dog', 'cat']:
            species = input('input a dog or a cat please ')
        name = input('what is its name')
        pet = f'{name},{species}'
        return pet
        
        
        

class Dog:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    def bark():
        print('woof im rex')
        



class Cat(Dog):
    def __init__(self, name, species):
        super().__init__(name)
        super().__init__(species)
    def meow():
        print('meow, im a mittens')
       



print('do you want to add or interact with a pet?')
def petprint():
    for pet in pets:
        return pet
    

def rerun():
    choice = 0
    while not choice:
        try:
            choice = int(input('type 1 to add pet\ntype 2 to interact with a pet\n'))
        except ValueError:
            choice = int(input('please enter 1 or 2'))
    if choice == 1:
        newpet = Petowner.addpet()
        pets.append(newpet)
        time.sleep(0.5)
        print('your new pet has been added')
        time.sleep(0.5)
        choice = 0
        rerun()
    elif choice == 2:
        pet = petprint()
        print('which pet do you want to pet',)
        for pes in pets:
            print(pes)
    thepet = input('input your pets name\n')
    if re.search(r'dog', thepet):
        Dog.bark()
        choice = 0
    elif re.search(r'cat', thepet):
        Cat.meow()
        choice = 0
    else:
         thepet = input('please input your pet\n')

if __name__ == '__main__':
    rerun()
    
        

    
