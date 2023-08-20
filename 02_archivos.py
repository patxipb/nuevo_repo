#ejemplos de manejo de ficheros

#archivo .txt
import os
txt_file = open("archivo.txt","a")
txt_file.write("Hola\n")
despedida = "Adios\n"
txt_file.write(despedida)
txt_file.close

txt_file = open("archivo.txt","r+")
for line in txt_file.readlines():
    print(line)

#archivo .json
import json

json_file = open("archivo.json", "w+")

json_test = {
    "nombre":"P",
    "apellidos":"PB",
    "coche":"Ford"
}

json.dump(json_test, json_file, indent=0)
json_file.close()

with open("archivo.json") as other_json_file: 
    for line in other_json_file.readlines():
        print(line)

json_dict = json.load(open("archivo.json"))
print(json_dict)
print(type(json_dict))
print(json_dict["nombre"])

#archivo .csv
import csv

csv_file = open("archivo.csv", "w+")

csv_writer = csv.writer(csv_file)
csv_writer.writerow(["nombre","apellidos","coche"])
csv_writer.writerow(["P","PB","Ford"])
csv_writer.writerow(["J","","Seat"])
csv_writer.writerow(["A","TH",""])

csv_file.close()

with open("./archivo.csv") as other_csv_file: #otro tipo de enrutamiento
    for line in other_csv_file.readlines():
        print(line)


#archivo .xml
import xml
