
class Telecom:
    def SetInfo(self,name,numberprefix):
        self.Name=name
        self.Numberprefix=numberprefix
        
    def show(self):
        print("Name: %s " % (self.Name))
        print("Numberprefix: %i " % (self.Numberprefix))
        

ListOfCompany=[]
sim=Telecom()
sim.SetInfo("BJ",21)
ListOfCompany.append(sim)

class smart(Telecom):
    pass
        
class globe(Telecom):
    pass

class sun(Telecom):
    pass


for sim in ListOfCompany:
    sim.show()

