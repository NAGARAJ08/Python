class Computer:

    def __init__(self,cpu,ram):
        # print("This is Computer")
        self.cpu = cpu
        self.ram = ram
    def configuration(self):
        print("Computer Specifics are: ",self.cpu,self.ram,"gb RAM")
        

comp1 = Computer("Intel i7",16)
comp2 = Computer("Ryzen",8)

# Computer.configuration(comp1)
comp1.configuration()

comp2.configuration()