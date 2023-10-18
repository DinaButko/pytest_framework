try:
    # r means read mode
    f = open(file="myfile.txt", mode = 'r')
    print(f.read())
    print(f.readline())
finally:
    f.close()

