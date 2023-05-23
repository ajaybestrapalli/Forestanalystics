import csv
import matplotlib.pyplot as plt
import numpy as np
arr = []
arr1 = []
arr2 =[]
with open("ForestArea.csv", 'r') as file:
  csvreader = csv.reader(file)
  k = 0
  for row in csvreader:
    if k > 1:
      if float(row[7]) > 1000:
       arr.append(float(row[7]))
       arr1.append(float(row[6]))
       arr2.append(float(row[6]) / float(row[7]))
    k = k + 1
  plt.scatter(arr, arr2)
  plt.show()

'''with open("Marine.csv", 'r') as file1:
  csvreader1 = csv.reader(file1)
  linen = 0
  print("Country -- Forest protected(%) -- Marine protected(%)")
  for row in csvreader1:
    if linen > 1:
      for x in arr:
        if x[0] == row[0]:
          print(x[1], "--", x[8],"--", row[3])
    linen = linen + 1'''
