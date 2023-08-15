x = 5

my_list = {5, 6, 7, 8}
my_list.add(9)

print(type(my_list))

for i in my_list:  
    print(i)

my_list = [5, 6, 7, 8]
my_list.append(9)
print(type(my_list))

for i in my_list:  
    print(i)


my_dict = dict()
my_dict = {"clave1":"valor", 
            "clave2":"valor2"}
print(my_dict.keys())
print(my_dict.values())

for i in my_dict:
    print(i) #asi obtenemos la clave
    print(my_dict[i]) #asi obtenemos el valor

for i in my_dict.keys():
    print(i)

for i in my_dict.values():
    print(i)

for clave, valor in my_dict.items():
    print(clave, valor)

print("Esto desde el movil")
print("Ahora un commit online")
