import random
class box:
  def __init__(self,length=0,breadth=None,height=None):
    self.length=length
    self.breadth=length if breadth is None else breadth
    self.height=length  if height is None else height
    self.area=0
    self.volume=0
  def calcarea(self):
    self.area=2*(self.length*self.breadth+self.breadth*self.height+self.height*self.length)
    return self.area
  def calcvol(self):
    self.volume = self.length*self.breadth*self.height
    return self.volume
n=int(input("Enter the number of boxes:"))
boxes=[]
for i in range(n):
  length=random.randint(1,10)
  breadth=random.randint(1,10)
  height=random.randint(1,10)
  bo=box(length,breadth,height)
  boxes.append(bo)
print("The details of the box with maximum volume area ratio is")
print("Length:",maxratio.length)
print("Breadth:",maxratio.breadth)
print("Height:",maxratio.height)
print("The maximum ratio is:",maxratio.calcvol()/maxratio.calcarea())
