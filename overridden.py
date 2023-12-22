class Parent(): 
      
    def show(self): 
        print("Inside Parent") 
          
class Child(Parent): 
      
    def show(self): 
          
        Parent.show(self) 
        print("Inside Child") 
          
obj = Child() 
obj.show() 
