lista=[]
file=open("devices.txt")
for i in file:
    i=i.strip()
    lista.append(i)
file.close()
print(lista)