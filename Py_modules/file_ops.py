try:
    # r means read mode
    f = open(file="myfile.txt", mode = 'r')
    print(f.read())
    print(f.readline())
finally:
    f.close()

print("""Using with Option""")
with open("myfile.txt",'r') as f:
    print(f.readline())
    list2 = f.read().split("\n")
    print(list2)



