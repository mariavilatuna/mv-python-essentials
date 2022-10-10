file = open("devices.txt","a")
while True:
    newItem =input("Ingrese un nuevo dispositivo: ")
    if newItem == "exit":
        print("Todo Listo!")
        break
    file.write(newItem + "\n")
file.close() 