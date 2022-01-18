import numpy as np
import csv
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

data = []
final_data = []

PathToFileData = ('/home/thanh/Documents/HW3/Salary_Data.csv')
with open(PathToFileData) as file:
    read_data = csv.reader(file)
    pocket = [i for i in read_data] #Data in each row
    pocket = np.array(pocket)
    row = pocket.shape[0] #number of rows
    column = pocket.shape[1] #number of columns 
#string to float 
for i in range(row):
    TEMP = []
    for j in range(column):
        temp = float(pocket[i][j])
        TEMP.append(temp)
    data.append(TEMP)
data = np.array(data) #matrix data

#Using sklearn
scaler = StandardScaler().fit(data) 
final_data = scaler.transform(data) 
print("Standardization: \n", final_data)


fig, (Before_Scale, After_Scale) = plt.subplots(1, 2)
fig.suptitle('Standardization')
Before_Scale.plot(data[:, 0], data[:, 1], 'ro')
After_Scale.plot(final_data[:, 0], final_data[:, 1], 'ro')
Before_Scale.set(title = 'original data', xlabel = 'Age', ylabel = 'Salary')
After_Scale.set(title = 'data after standardizing', xlabel = 'Age', ylabel = 'Salary')
plt.show()
