# Función para determinar el rango de la VLAN
def verificar_vlan(numero_vlan):
    if 1 <= numero_vlan <= 1005:
        return "VLAN del rango normal"
    elif 1006 <= numero_vlan <= 4094:
        return "VLAN del rango extendido"
    else:
        return "Número de VLAN fuera del rango permitido (1-4094)"

# Solicitar al usuario el número de VLAN
try:
    vlan_input = int(input("Ingrese el número de VLAN: "))
    resultado = verificar_vlan(vlan_input)
    print(resultado)
except ValueError:
    print("Por favor, ingrese un número válido.")

