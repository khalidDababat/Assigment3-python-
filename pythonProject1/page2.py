import MyModule
import os

print(os.getcwd())



Data_FIle = "khalid.txt"

#print(MyModule.read_txt_file(Data_FIle))  ***** Print The Dictionary Info
for key,value in MyModule.read_txt_file(Data_FIle).items():
    print(key,value)


MyModule.read_txt_file(Data_FIle)




