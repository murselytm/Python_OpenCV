setA ={1,2,3,4,5}
setB = {1,3,4,6,7,8}

print(setA | setB)
print(setA.union(setB))

print(setA & setB)
print(setA.intersection(setB))

print(setA - setB)
print(setA.difference(setB))
print(setB.difference(setA))

print(setA ^ setB)
print(setA.symmetric_difference(setB))