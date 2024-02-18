import json
import math
import os
from unittest.util import sorted_list_difference


def data_to_dict(file_path):
   try:
      with open(file_path,"r") as file:
          # Create A new Dicitinary
          dic_data = {}
          for i in file:
              parts = i.strip().split(",")
              name = parts[0]
              marks = [int(marks) for marks in parts[1:]]
              dic_data[name] = marks
          return dic_data
   except Exception as e:
       return e



def getmaxAvgstudent(dici):
    '''
      This function taks a list of marks for each student a return the maximum avg.
      and student name
      :param dictionary: dictionary of data
      :return: list contains student name and Average
      '''
    try:
       maxAvg = None
       maximum = []

       for  Name,listmarks in dici.items():
           sumMarks =0

           for mark in listmarks:
               sumMarks += mark
           AvgM =sumMarks/len(listmarks)
           if maxAvg == None or AvgM >maxAvg:
                maxAvg = AvgM
                maximum.clear()
                maximum.append([Name ,maxAvg])
       return maximum
    except Exception as e:
        return e

def  getminAvgstudent(dici):
    try:

        minAvg = None
        minmum =[]
        for name ,listmarks in dici.items():
            sumM = 0
            for mark in listmarks:
                sumM += mark
            AvgM = sumM/len(listmarks)
            if(minAvg == None or minAvg > AvgM):
                minAvg =AvgM
                minmum.clear()
                minmum.append([name,AvgM])
        return minmum


    except Exception as e:
        print(e)



def getmaxmarkstudent(dici):
    try:
        maxmark = 0
        maximuMark =[]
        for name ,listmarks in dici.items():

            for mark in listmarks:
                if mark > maxmark:
                    maxmark =mark
                    maximuMark.clear()
                    maximuMark.append([name,maxmark])
        return maximuMark



    except Exception as e:
        return e

def getminmarkstudent(dici):

    try:

            minmark = None
            minmumMark = []
            for name, listmarks in dici.items():
                for mark in listmarks:
                    if minmark ==None or mark < minmark:
                        minmark = mark
                        minmumMark.clear()
                        minmumMark.append([name, minmark])
            return minmumMark

    except Exception as e:
        print(e)
        return None




def StandardDeviation(listOfMark):
    '''
    This function calculates the Standard deviation of the marks takes dictionary
    as input and return the Standard deviation
    :param list: listOfMark of data
    :return: Standard deviation value
    '''


    try:
        sum = 0
        count = 0
        for mark in listOfMark:
            sum += mark
            count += 1
        mean= sum / count
        sum =0
        for x in listOfMark:
            sum += math.pow(x-mean,2)
        std = round(math.sqrt(sum/len(listOfMark))-1)
        return std
    except Exception as e:
        print(e)


def sortValues(listOfMark):

    try:
       n = len(listOfMark)
       for i in range(n):
           for j in range(0 ,n-i-1):
               if(listOfMark[j] >listOfMark[j+1]):
                   listOfMark[j],listOfMark[j+1] = listOfMark[j+1],listOfMark[j]
       return listOfMark

    except Exception as e:
        print(e)
        return None


def calculate_median(sorted_list):
      '''
           this function calculate the median
           :param sorted_list: sorted list of values
           :return: median Value
           '''
      try:
          if len(sorted_list)%2 == 0:
              return (sorted_list[len(sorted_list)//2- 1] + sorted_list[len(sorted_list) // 2])/2
          else:
              return sorted_list[len(sorted_list)//2]

      except Exception as e:
           print(e)


def quartiles(listofmarks):

     try:
         # sort the values
         sorted_list_of_values = sortValues(listofmarks)
         # find Q2
         Q2 =calculate_median(sorted_list_of_values)

         # split the data into two halfs
         if len(sorted_list_of_values) % 2 == 0:
             upper_half = sorted_list_of_values[len(sorted_list_of_values) // 2:]
             lower_half = sorted_list_of_values[:len(sorted_list_of_values) // 2]
         else:
             upper_half = sorted_list_of_values[len(sorted_list_of_values) // 2 + 1:]
             lower_half = sorted_list_of_values[:len(sorted_list_of_values) // 2]

         # find Q1 and Q3
         Q1 = calculate_median(lower_half)
         Q3 = calculate_median(upper_half)
         return [Q1,Q2,Q3,(Q3-Q1)]
     except Exception as e:
         print(e)


def get_most_frequent_mark(listofAllmarks):
    '''
      This function return the most frequent mark
      :param dict: list  of All marks
      :return: most frequent mark
      '''
    try:

        max = 0
        most_frec_mark = None
        dict_of_frec = {}
        for item in listofAllmarks:
            if item in dict_of_frec:
                dict_of_frec[item] += 1
            else:
                dict_of_frec[item] = 1
        for key, value in dict_of_frec.items():
            if value > max:
                max = value
                most_frec_mark = key
        return most_frec_mark


    except Exception as e:
        print(e)



def CreateJsonFile(filename ,dec_output):
    try:
        with open(filename, "w") as file:
            json.dump(dec_output, file,indent=4)

    except Exception as e:
        print(e)
