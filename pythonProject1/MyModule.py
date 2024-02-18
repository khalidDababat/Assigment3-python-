import os


# Create an empty dictionary to store the data
student_marks = {}
def read_txt_file(txt_path):
    try:
        with open(txt_path,"r") as file:
         for line in file:
            data = line.strip().split(",") # [list]
            student_name =data[0]
            marks = [int(mark) for mark in data[1:]] # Converts marks To Integers
            student_marks[student_name] = marks

         return student_marks

    except Exception as e:
        print(e)