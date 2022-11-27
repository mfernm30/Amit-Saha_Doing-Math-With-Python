try: 
    a = float(input('Enter a number: '))
except ValueError: # ValueError Exception 
    print('You entered an invalid number')


a = input('Input an Integer: ')

a = int(input('Input an Integer: ')) # Como la función int(String) si el string es un entero se puede realizar la conversión pero si es un float da un error de valor

# Se utiliza la siguiente función para filtrar numeros no enteros pero guardando los que se comportan como enteros 1.0, 2.0 ...

print(1.1.is_integer()) # Return False
print(1.0.is_integer()) # Return True