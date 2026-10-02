class Duck:
    def eat(self):
        print(" Duck is eating...")
        
class Dog:
    def eat(self):
        print(" Dog is eating...")
        
def animal_is_eating(animal):
    animal.eat()
    
animal_is_eating(Duck())
animal_is_eating(Dog())