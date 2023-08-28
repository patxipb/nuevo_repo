### ejemplos de tipos de estructuras
x = 5
print("-----------\n")
#set
my_set = {5, 6, 7, 8}
print(type(my_set))

my_set.add(9)
for i in my_set:  
    print(i)

print("-----------\n")
#list
my_list = [5, 6, 7, 8]
print(type(my_list))

my_list.append(9)
for i in my_list:  
    print(i)

print("-----------\n")
#tuplas
my_tuple = (1,2,3,4)
print(type(my_tuple))

for i in my_tuple:
    print(i)    

print("-----------\n")
#dict
my_dict = dict()
print(type(my_dict))

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


