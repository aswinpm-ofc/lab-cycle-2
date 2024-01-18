class TDShapes:
  def printArea(area):
    print("Area is:",area)
  def printVolume(volume):
    print("Volume is:",volume)
class Cylinder(TDShapes):
  def calcarea(r,h):
    area=2*3.14*r*h+2*3.14*r**2
    return area
  def calcvol(r,h):
    volume=3.14*r**2*h
    return volume
class Sphere(TDShapes):
  def calcarea(r):
    area=4*3.14*r**2
    return area
  def calcvol(r):
    volume=(4/3)*3.14*r**3
    return volume
radius=float(input("Enter the radius:"))
height=float(input("Enter the height:"))
c=Cylinder
c1=c.calcarea(radius,height)
c2=c.calcvol(radius,height)
print("CYLINDER")
c.printArea(c1)
c.printVolume(c2)
s=Sphere
s1=s.calcarea(radius)
s2=s.calcvol(radius)
print("SPHERE")
s.printArea(s1)
s.printVolume(s2)
