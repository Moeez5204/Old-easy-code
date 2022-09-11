class animal():

    def __init__ (self):

        species = "unknown"
        age = 0
        Hunger_Level = 0
        Threath = "peaceful"

    def setSpecies(self):
        self.species = input("input species")

    def setAge(self):
        self.age = int(input("input age"))

    def setHunger(self):
        self.hunger = int(input("Input hunger"))


    def ChangeThreath(self):
        if self.hunger < 3:
            self.Threath = "peacful"
        elif self.hunger >= 3 and self.hunger <=7:
            self.Threath = "narky"
        else:
            self.Threath = "agrresive"

        print(self.Threath)
    

cat = animal()
cat.setSpecies()
cat.setAge()
cat.setHunger()
cat.ChangeThreath()
        


    
    
       
