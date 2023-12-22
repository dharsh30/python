people = {"Jay", "Trish", "Arav"}
print("People:", end = ' ' )
print(people)
people.add("sam")
for i in range(1, 6):
    people.add(i)
print(people)
    
    
people1 = {"Jay", "Idrish", "Archil"}
vampires = {"Karan", "Arjun"}
dracula = {"Deepanshu", "Raju"}
population = people1.union(vampires)
print(population)
population = people1|dracula
print(population)