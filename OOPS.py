class car:
    def__init__(self,length,breadth):
         self.length=length
         self.breadth=breadth
    def setlength(self, length):
         self.length = length
    def setbreadth(self,breadth):
        self.breadth=breadth
    def getlength(self):
        return self.length
    def getbreadth(self):
        return self.breadth
    def Area(self):
        return self.length*self.breadth
    def perimeter(self):
        return 2*(self.length+self.breadth)

