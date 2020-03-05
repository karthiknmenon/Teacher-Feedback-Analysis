import matplotlib.pyplot as plt
import csv
x=[]
y=[]
with open('csvfile1', 'r') as csvfile:
    plots= csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        #print(x)
        y.append(int(row[1]))
plt.plot(x,y, marker='o')
plt.title('Data from the CSV File: Days of the week and Garbage Generated')
plt.xlabel('Day of the week')
plt.ylabel('Garbage Generated')

plt.show()