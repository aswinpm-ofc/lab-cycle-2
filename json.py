import json
f=open("iris.json","r")
fl=f.read()
print("The list having each line of the file as element is")
print(fl)
ld = json.loads(fl)
print("The list of dictionary objects is")
print(ld)
print("Details of flower species setosa is")
for d in ld:
  if d["species"]=="setosa":
    print("\n",d)
z=[]
p=[]
x=[]
y=[]
c=[]
e=[]
for d in ld:
  if d["species"]=="setosa":
      a=list(d.values())
      searea=a[0]*a[1]
      z.append(searea)
      pearea=a[2]*a[3]
      p.append(pearea)
print("maximum sepal area in setosa is:",max(z))
print("minimum sepal area in setosa is:",min(z))
print("maximum petal area in setosa is:",max(p))
print("minimum petal area in setosa is:",min(p))
for d in ld:
  if d["species"]=="versicolor":
      a=list(d.values())
      searea=a[0]*a[1]
      x.append(searea)
      pearea=a[2]*a[3]
      y.append(pearea)
print("maximum sepal area in versicolor is:",max(x))
print("minimum sepal area in versicolor is:",min(x))
print("maximum petal area in versicolor is:",max(y))
print("minimum petal area in versicolor is:",min(y))
for d in ld:
  if d["species"]=="virginica":
      a=list(d.values())
      searea=a[0]*a[1]
      c.append(searea)
      pearea=a[2]*a[3]
      e.append(pearea)
print("maximum sepal area in virginica is:",max(c))
print("minimum sepal area in virginica is:",min(c))
print("maximum petal area in virginica is:",max(e))
print("minimum petal area in virginica is:",min(e))

sl=sorted(ld,key=lambda x:x["sepalLength"]*x["sepalWidth"]+x["petalLength"]*x["petalWidth"])
print("Sorted list of dictionaries according to total area")
for flower in sl:
    print(flower)
