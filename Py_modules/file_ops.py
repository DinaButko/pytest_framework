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

print("""Using with Option but with split""")
with open("myfile.txt",'r') as f:

    for line in f:
        print(line.strip())

