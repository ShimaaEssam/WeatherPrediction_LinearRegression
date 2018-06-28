import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import sys

day = int(sys.argv[1])
month = int(sys.argv[2])
year=int(sys.argv[3])
place=str(sys.argv[4])
normalization = MinMaxScaler()  # load MIN_Max_Scaler


def read_dataset():

    if place=="Cairo":
      data = pd.read_excel("C:\Users\LENOVO\PycharmProjects\untitled\Cairo.xlsx")#read_dataset
    elif place=="Assuit":
     data = pd.read_excel("C:\Users\LENOVO\PycharmProjects\untitled\Assuit.xlsx")#read_dataset
    elif place=="Alexandria":
     data = pd.read_excel("C:\Users\LENOVO\PycharmProjects\untitled\Alexandria.xlsx")#read_dataset
    elif place=="Asswan":
     data = pd.read_excel("C:\Users\LENOVO\PycharmProjects\untitled\Asswan.xlsx")#read_dataset
    elif place=="Hurghada":
     data = pd.read_excel("C:\Users\LENOVO\PycharmProjects\untitled\Hurghada.xlsx")#read_dataset
    elif place=="Ismailia":
      data = pd.read_excel("C:\Users\LENOVO\PycharmProjects\untitled\Ismailia.xlsx")#read_dataset
    elif place=="portSaid":
      data = pd.read_excel("C:\Users\LENOVO\PycharmProjects\untitled\portSaid.xlsx")#read_dataset

   # print(data['Month'].unique())  # print unique months in month's column

    data['Month'] = data['Month'].replace(('oct'), ('Oct'))  # repair dataset
    data['Month'] = data['Month'].replace((' Apr'), ('Apr'))  # repair dataset
    data['Month'] = data['Month'].replace((' June'), ('June'))  # repair dataset
    data['Month'] = data['Month'].replace(('Sept'), ('Sep'))  # repair dataset
    data['Month'] = data['Month'].replace(( "' June'"), ('June'))  # repair dataset
    data['Month'] = data['Month'].replace(("' Apr'"), ('Apr'))  # repair dataset

    months = np.asarray(data['Month'].unique())  # take unique months# remove duplicated
    days = np.asarray(data['Day'].unique())  # take unique months
    years = np.asarray(data['Year'].unique())  # take unique months
    #print(months)
    #print(days)
    #print(years)

    # for i, month in enumerate(months):#replace each month with numeric value
    #     data['M'] = data['M'].replace(month, i+1)
    data['Month'] = data['Month'].replace(
        ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'),
        (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))  # hardcode
    #print(data['Month'])

    x = data[['Year', 'Month', 'Day']]  # input

    #x = data[['M']] #input

    y = data["Humidity_avg"] #output

    x = np.asarray(x)#put x in array
    y = np.asarray(y)#put y in array

    # x = normalization.fit_transform(x)#normalize input

    train_x, test_x, train_y, test_y = train_test_split(x, y, test_size=0.2, random_state=50)

    return x, y, train_x, test_x, train_y, test_y


x, y, train_x, test_x, train_y, test_y = read_dataset()

#plooooooooooooot
#plt.scatter(x[:,1], y, color='blue')
#plt.show()
#classification
lr = LinearRegression()#load LinearRegression

lr.fit(train_x, train_y)#Train model

predicted = lr.predict(test_x)#test model

error = np.sum(predicted - test_y)
#print(error)
#indiv test

#X[0] = [1996 ,1 ,1]
#y[0] = 20

input = [[year, month, day]]
# input_normalized = normalization.transform(input)
hum = lr.predict(input)
print(hum)

#plot test

#plt.scatter(test_x[:,1], test_y,  color='blue')
#plt.plot(test_x[:,1], predicted, color='black')
#plt.xticks(())
#plt.yticks(())
#plt.show()
