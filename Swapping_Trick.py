data_a = open("File 1.txt" , "r")

data_b = open("File 2.txt" , "r")

with open("File 1.txt" , "r") as a:
 data_a = a.read()

with open("File 1.txt" , "w") as a:
 a.write(data_b)