# using try except block

import csv 
try:
    with open ('data4.csv','r') as f5:
        cv=csv.writer(f5, delimiter=',')
        for c in cv:
            print(c)
except FileNotFoundError:
    print('file not found')