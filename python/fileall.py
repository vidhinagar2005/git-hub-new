file = open("afile.txt","w")
file.write("Hello world! abcdefg")
file.write("\nwelcome...")
file.close()

#with statement automatically open and close file
with open("afile.txt","r") as file:
    content = file.read() 
    print(content)

#read file only 10 lines and so on
with open("afile.txt","r") as file:
    content = file.read(10)
    print(content)

#readline() read single line
with open("afile.txt","r") as file:
    line = file.readline()
    print(line)

#readlines() read all lines
with open("afile.txt","r") as file:
    line = file.readlines()
    print(line)

#write string to file
with open("afile.txt","w") as file:
    file.write("this is a text file")
    file.write("new file extend")

#write a list into a file
lines = ["line 1\n"," line2"," \n line3"]
with open("afile.txt","w") as file:
    file.writelines(lines)
    

#append lines
with open("afile.txt","a") as file:
    file.write("new lines...")