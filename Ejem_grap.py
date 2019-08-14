import os

f = open("grap.txt", "w")

f.write("digraph G {\n")
f.write("node [shape = square];\n")
l = ["A1", "B2","C3","D4","E5", "F6"]
for i in range(len(l)-1):
	f.write("\""+ l[i]+ "\"->\"JUAN\";\n")
    #print(l[i])
f.write("}")
f.close()

os.system("dot -Tpng grap.txt -o grap.jpg")
os.system("grap.jpg")