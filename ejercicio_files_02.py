file=open("devices.txt")
for i in file:
    i=i.strip() #La función strip elimina los espacios iniciales y finales de la cadena
    print(i)
file.close()
