

try:

    with open("data.txt","r") as file:


        dic_data = {}
        for line in file:
            parts = line.strip().split(',')
            name = parts[0]
            marks = [int(marks) for marks in parts[1:]]
            dic_data[name] =marks
        print(dic_data)

    listAllMarks = []
    for listM in dic_data.values():
        listAllMarks += listM
    print(listAllMarks)
except Exception as e:
    print(e)
