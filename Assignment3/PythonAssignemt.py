
import json
import MyFunction as m

path = "data.txt"

#print(m.data_to_dict(path))
dec_data = {}
dec_data =m.data_to_dict(path)

listAllmarks = []
for mark in dec_data.values():
    listAllmarks += mark

#print(m.StandardDeviation(listOfMark=listAllmarks))
#print(m.sortValues(listOfMark=listAllmarks))

#print(m.quartiles(listofmarks=listAllmarks))

#print(m.get_most_frequent_mark(listAllmarks))


dic_output = {

    "MaxValue": {
        "student_name": str(m.getmaxmarkstudent(dec_data)[0][0]),
        "value": str(m.getmaxmarkstudent(dec_data)[0][1])
    },
    "MaxAvg": {
        "student_name": str(m.getmaxAvgstudent(dec_data)[0][0]),
        "value": str(m.getmaxAvgstudent(dec_data)[0][1])
    },

    "MinValue": {
        "student_name": str(m.getminmarkstudent(dec_data)[0][0]),
        "value": str(m.getminmarkstudent(dec_data)[0][1])
    },
    "MinAvg": {
        "student_name": str(m.getminAvgstudent(dec_data)[0][0]),
        "value": str(m.getminAvgstudent(dec_data)[0][1])
    },

    "standard_deviation": str(m.StandardDeviation(listOfMark=listAllmarks)),
    "Q1": str(m.quartiles(listofmarks=listAllmarks)[0]),
    "Q2": str(m.quartiles(listofmarks=listAllmarks)[1]),
    "Q3": str(m.quartiles(listofmarks=listAllmarks)[2]),
    "IQR": str(m.quartiles(listofmarks=listAllmarks)[3]),
    "most_freq_value": str(m.get_most_frequent_mark(listAllmarks))

}
#print(dic_output)

m.CreateJsonFile("Output_dec",dic_output)