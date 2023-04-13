# wap to send one record in a csv file.

import csv
f1=open('data.csv','w')
cv=csv.writer(f1, delimiter=',')
cv.writerow(['Team','Score'])
cv.writerow(['A',89])
cv.writerow(['B',79])
cv.writerow(['C',91])
print("file created")

