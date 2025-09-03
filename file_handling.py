# file=open("demo.txt",mode="r")
# c=file.read() 
# print(c)
# file.close()

#   or

# c=file.read(3)
# print(c)
# file.close()

# file=open("demo.txt",mode="r")
# c=file.readline() 
# print(c)
# file.close()

# file=open("demo.txt",mode="r")
# c=file.readlines(2) 
# print(c)
# file.close()

# file=open("demo.txt",mode="a")
# c=file.write(" This is append mode") 
# file.close()

# #Reading file in "r+" mode:
# with open("demo.txt","r+") as fd:
#     print(fd.tell())
#     print(fd.read())
#     print(fd.tell())

#Reading file in "w+"mode:
# with open("demo.txt","w+") as fd:
#     print(fd.tell())
#     c=fd.write("this is w+")
#     print(fd.read())
#     print(fd.tell())

# #write file in "r+" mode:
# with open("demo.txt","r+") as fd:
#     fd.write("new text>")

# #write file in "w+" mode:
# with open("demo.txt","w+") as fd:
#     fd.write("New text.")

# #Opening filein "w+" mode when it does not exist
# with open("sample1.txt","w+") as fd:
#     pass

# # Opening file
# fp=open("demo.txt","r")
# print(fp.tell())
# fp.read(2)
# #Print the posiotion of handle
# print(fp.tell())
# fp.seek(0)
# print(fp.tell())
# # file closing
# fp.close()

# file=open("demo.txt",mode="r+")
# convert=file.read()
# v=str(convert) 
# print(v)
# f=v.split()
# print(f)
# f.insert(2,'chetan')
# print(file.tell())
# file.close()
# file=open("demo.txt",mode="w")
# print(f)
# for i in f:
#     file.writelines([i])
 
