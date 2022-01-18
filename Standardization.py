import numpy as np
import csv
import matplotlib.pyplot as plt

data = []
final_data = []

##Data processing
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

###Standardization (feature normalization with zero mean and unit variance)
final_data = data.copy()
#x' = (x - x_average)/xichma |||| x_average = mean, xichma(standard deviation) = sqrt(full(error)^2/n)

##Standardization Column 1
#Calculating mean
sum = 0
for i in range(row):
    sum += data[i][0]
mean = sum / row #x_average
#Calculating standart deviation
sum_error = 0
for i in range(row):
    sum_error += (data[i][0] - mean) ** 2
standard_deviation = (sum_error/row) ** (1/2)
#Normalized value
for i in range(row):
   final_data[i][0] = (data[i][0] - mean) / standard_deviation

##Standardization Column 2
#Calculating mean
sum = 0
for i in range(row):
    sum += data[i][1]
mean = sum / row #x_average
#Calculating standart deviation
sum_error = 0
for i in range(row):
    sum_error += (data[i][1] - mean) ** 2
standard_deviation = (sum_error/row) ** (1/2)
#Normalized value
for i in range(row):
    final_data[i][1] = (data[i][1] - mean) / standard_deviation

print('Data after standardizing:')
print(final_data) 
##Draw graph
fig, (Before_Scale, After_Scale) = plt.subplots(1, 2)
fig.suptitle('Standardization')
Before_Scale.plot(data[:, 0], data[:, 1], 'ro')
After_Scale.plot(final_data[:, 0], final_data[:, 1], 'ro')
Before_Scale.set(title = 'original data', xlabel = 'Age', ylabel = 'Salary')
After_Scale.set(title = 'data after standardizing', xlabel = 'Age', ylabel = 'Salary')
plt.show()









