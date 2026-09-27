#Selecciona un problema sencillo de la vida real para resolver con programación.
"""Se escogió realizar una agenda telefónica"""


lista_contactos = []
        
def agregar_contacto():#Agrega un nuevo contacto al diccionario con teléfono y una categoría
    nombre = input("Ingrese nombre del nuevo contacto:              ")
    teléfono = input("Ingrese el número de teléfono:                ")
    categoría = input("Ingrese una categoria (Familia,trabajo,etc): ")
    try:
        contacto = [nombre, teléfono, categoría]
        lista_contactos.append(contacto)
        print("")
        print ("✅ El Contacto", nombre ,"se ha guardado con éxito.")
        print("")
    except ValueError:
        print("Erro al guardar")
         
def modificar_contacto():#Operación adicional: Eliminar un contacto del diccionario.
    nombre = input("Ingrese el contacto que desa modificar: ")
    for contacto in lista_contactos:
        if contacto[0] == nombre:
            nombre = input("Ingrese el nombre:                            ")
            contacto[0] = nombre
            teléfono = input("Ingrese su numero de teléfono:              ")
            contacto[1] = teléfono
            categoría = input("Ingrese su categoría (Familia,trabajo,etc: ")      
            contacto[2] = categoría 
            print("")
            print("Se actualizo con exito el contacto", nombre)
            print("")
            break
        else:
            print("")
            print(f"❌ No se encontró el contacto ", nombre)
            print("")
        break

def mostrar_contactos():#Recorre y muestra de forma clara la información almacenada.
    for contacto in lista_contactos:
        print("")
        print(f"Nombre:      {contacto[0]}\n"
              f"Teléfono:    {contacto[1]} \n"
              f"Categoría:   {contacto[2]}")
        print("")

def buscar_contacto():#Operación adicional: busca un contacto del diccionario.
    nombre = input("Ingrese el nombre del contacto: ")
    for contacto in lista_contactos:
        if contacto[0] == nombre:
            print("")
            print(f"Nombre:     {contacto[0]}\n"
                  f"Teléfono:   {contacto[1]} \n"
                  f"categoría:  {contacto[2]}")
            print("")

def eliminar_contacto():#:nombre):#Operación adicional: Elimina un contacto del diccionario.
    nombre = input("Ingrese el contacto que desea borrar:   ")
    for contacto in lista_contactos:
        if contacto[0]== nombre:
            lista_contactos.remove(contacto)
            print("")
            print("El contacto", nombre, "se elimino con exito 🗑️ ")
            print("")
            break
        else:
            print("")
            print(f"❌ No se encontró el contacto ", nombre )   
            print("")          

while True:
    print("")
    print("*******   Sistema de Regsitro de contactos tefónicos    ****************")
    print("           Menu Principal                   ")
    print("      1. 👤  Agregar un contacto")
    print("      2.     Modificar un contacto")
    print("      3. 🔎  Buscar un contacto")
    print("      4.      Mostrar los contacto")
    print("      5. 🗑️  Eliminar un contacto")
    print("      6.      Salir")
    print("")
    opcion = int(input("Ingrese el numero de la opcion: "))
    match opcion:
        case 1:
            agregar_contacto()            
        case 2:
            modificar_contacto()
        case 3:
            buscar_contacto()
            #print("-"*50)
        case 4:
            mostrar_contactos()                   
            print("-"*50)
        case 5:
            eliminar_contacto()
            print("-"*50)
        case 6:
            print("\n 👋 ¡Gracias por usar la Agenda de Contactos! Hasta luego.")
            break
        case _:
            print(" ⚠️  Opción inválida. Intente de nuevo")