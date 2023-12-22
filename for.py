n = 4
for i in range(0, n):
    print(i)
    
print("List Iteration")
l = ["s", "for", "Hexware"]
for i in l:
    print(i)
print("\nTuple Iteration")

t = ("Hexware", "for", "Hexware")
for i in t:
    print(i)
print("\nString Iteration")
s = "Hexware"
for i in s:
    print(i)
print("\nDictionary Iteration")
d = dict()
d['xyz'] = 50
d['abc'] = 100
for i in d:
    print('%s%d,%i' (i, d[i]))
print("\nSet Iteration")
set1 = {1, 2, 3, 4, 5, 6}
for i in set1:
  print(i),