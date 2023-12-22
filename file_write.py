with open("file.txt", "w") as f: 
    f.write("Hello there ")

file = open('file.txt', 'a')
file.write("This will add this line")
file.close()