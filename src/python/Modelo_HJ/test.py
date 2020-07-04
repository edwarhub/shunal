import  detect

idClass = detect.main("images",0.5,0.5,["data/images/test1.jpg"])
print("Hola")
print(idClass)

if 'person' in idClass:
    print("Sospechoso detectado")