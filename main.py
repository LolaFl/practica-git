from object import MaquinaJoyeria

def menu():
    print("\n--- Menú de Máquina de Joyería ---")
    print("1. Encender máquina")
    print("2. Apagar máquina")
    print("3. Fabricar joya")
    print("4. Ver información de la máquina")
    print("5. Salir")

maquina = MaquinaJoyeria("JewelryTech", "Model X", "Oro")

while True:
    menu()
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        maquina.encender()
    elif opcion == "2":
        maquina.apagar()
    elif opcion == "3":
        tipo_joya = input("Introduce el tipo de joya a fabricar (anillo, collar, pulsera): ")
        maquina.fabricar_joya(tipo_joya)
    elif opcion == "4":
        print(maquina)
    elif opcion == "5":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida, intenta de nuevo.")