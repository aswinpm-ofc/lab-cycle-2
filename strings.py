s=input("Enter the numbers separated by space:")
l=list(map(int ,s.split()))
k=int(input("Enter the number of times to rotate:"))
roind=len(l)%k
for i in range(len(l)-roind,len(l)):
  l.append(l[i])

f=tuple([i for i in l])
tup=list(set(l))
li=[x**2-x for x in tup]
tup.sort()
li.sort()
sortl=tup+li
print("Rotated list is:",l)
print("Tuple list after list comprhension:",f)
print("List conatining no duplicates:",tup)
print("List after evaluation of the function:",li)
print("Merged list after sorting:",sortl)
