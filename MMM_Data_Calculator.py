#Imports

import csv
from collections import Counter

with open("SOCR-HeightWeight.csv", newline = "")as f:
  reader = csv.reader(f)
  file_data = list(reader)

file_data.pop(0)

new_data = []
for i in range(len(file_data)):
  number = file_data[i][2]
  new_data.append(float(number))

Input = input("Type in desired MMM data type e.g. Mean, Median and Mode : ")

#///!!Mean!!//

n = len(new_data)

if Input == "Mean":

    total = 0

    for x in new_data:
        total = total + x

    mean = total/n 

    print("Mean is ->", mean)

#///!!Median!!///

if Input == "Median":

    new_data.sort()
    if n % 2 == 0:
        median1 = float(new_data[n//2])
        median2 = float(new_data[n//2 + 1])
        median = (median1 + median2) / 2

    else:
        median = new_data[n//2]

    print("Mode is ->", median)

#///!!Mode!!///

if Input == "Mode":

    data = Counter(new_data)
    mode_data_for_range = {"50-60": 0, "60-70": 0, "70-80":0}

    for weight, occurance in data.items():
        if 50 < float(weight) < 60:
            mode_data_for_range["50-60"] += occurance

        elif 60 < float(weight) < 70:
            mode_data_for_range["60-70"] += occurance
    
        elif 70 < float(weight) < 80:
            mode_data_for_range["70-80"] += occurance

    mode_range, mode_occurence = 0, 0 
    for range, occurence in mode_data_for_range.items(): 

        if occurence > mode_occurence: 
            mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence 

    mode = float((mode_range[0] + mode_range[1]) / 2) 

    print(f"Mode is -> {mode:2f}")
    