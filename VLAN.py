
nro = int(input('Ingrese el numero de vlan:'))

if nro > 1 and nro < 1006:
    print("el valor de",nro,"corresponde a una VLAN normal")

elif nro > 1005 and nro < 2006:
    print("el valor de",nro,"corresponde a una VLAN extendida")

else:
    print('El valor ingresado no es valido')
