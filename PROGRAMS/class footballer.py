class fruit():
    def __init__(self,name,size,taste,color):
        
        self.name = name
        self.color = color
        self.size  = size
        self.taste = taste


    def description(self):
        print(self.name,'is',self.color,'and taste ',self.taste,'. Also it is ',
              self.size,'size')

class tropical(fruit):
        def __init__(self,name,size,taste,color):
            super().__init__(name,size,"sweet",color)

class citrus(fruit):
        def __init__(self,name,size,taste,color):
            super().__init__(name,size,"sweet",color)



            


mango = tropical('mango','medium','sweet','red')

lemon = citrus('lemon','small','bitter','yelllow')

mango.description()
lemon.description()
     
        
        
        
