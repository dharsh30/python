class father:
    def quality(self):
        print('father is intelligent')
     
    def nature(self):
        print('father is Strict')   
obj1=father()

class son1(father):
    
    def son1_quality(self):
        print('child wants to be a engineer')
obj2=son1() 
obj2.quality()
obj2.son1_quality()

class son2(father):
    
    def son2_quality(self):
        print('child wants to be a doctor')
obj3=son2() 
obj3.nature()
obj3.son2_quality()
      