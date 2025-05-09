class animal:
    def speak(self):
        return "I make a sound"
        
class Dog (animal):
    def speak(self):
        return "woof"
    class cat(animal):
        def speak (self):
            return "Meaow"
        
        
        #polymorphism in action0
        def make_animal_speak  (Dog,Cat):
            print(animal.speak( ))