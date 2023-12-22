class Bird:
    def __init__(self,name):
        self.name=name
    def info(self):
        print('this bird is', self.name)
    def fly(self):
        print('thr bird can fly')

class Parrot(Bird):
    def __init__(self,name,color,character):
        super().__init__(name)
        self.color=color
        self.character=character
    def info(self):
        super().info()
        print('color is',self.color)
        print('character is',self.character)
    
    def fly(self):
        print('the bird can fly')
        
obj_Parrot= Parrot('parrot','green','good')
obj_Parrot.fly()
obj_Parrot.info()
    