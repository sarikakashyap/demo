a=input("enter text \n")



path="C:/Users/Nakul/Desktop/python"
##file_handling=open(path+"/text_file.txt","r")
##print(file_handling.read())

#file_handling.close()
file=open(path+"/text_file.txt","a")
f=file.write(a +"\n")
file.close()
