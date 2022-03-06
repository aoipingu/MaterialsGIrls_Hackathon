# MaterialsGIrls_Hackathon
Repository for the 2022 24 hour WSET Hackathon Code




import os 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def get_data():
#function that takes data from csv file containing materials and all their properties and converts to a dataframe
#converts each column in dataframe to a list of the values of a particular property for each material
#creates dictionary where key is propoerty name as a string, and value is list of values for each material
      
    df = pd.read_csv('MaterialsGirls_Hackathon/one/materials.csv')

    Cost = df['Cost'].tolist()
    Density = df['Density'].tolist()
    E = df['E'].tolist()
    G = df['G'].tolist()
    v = df['v'].tolist()
    YieldStress= df['YieldStress'].tolist()
    UTS = df['UTS'].tolist()
    Breakingstrain = df['Breakingstrain'].tolist()
    Kc = df['Kc'].tolist()
    ThermalExpansion = df['ThermalExpansion'].tolist()
    FreshwaterUse = df['freshwateruse'].tolist()
    CarbonFootprint = df['Carbonfootprint'].tolist()

    values_list = [Cost, Density, E, G, v, YieldStress, UTS, Breakingstrain, Kc, ThermalExpansion, FreshwaterUse, CarbonFootprint]
    keys_list = df.columns.tolist()
    properties_dictionary = dict(zip(keys_list, values_list))

    return properties_dictionary





def choose_graph():
#function that lets user pick the inputs for the x axis and y axis for a graph
    properties_dictionary = get_data()
    print(f'Your choices are {df.columns.tolist()}')
    x = input('Enter your x-axis:')
    y = input('Enter your y-axis:')
    
    for i in properties_dictionary:
        if i ==x:
            return i 

    for j in properties_dictionary:
        if j ==y:
            return j




def plot_graph():
#function that plots the graph that was requested
    i,j = choose_graph()
    properties_dictionary = get_data()
    assert i!=j, 'cannot plot variable against itself'
   

    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.plot(i,j,'go-',)
    plt.xlabel(i)
    plt.ylabel(j)
    plt.title(f'{j} vs {i}')  

#labels each plot point with the material it belongs to
    ax = fig.add_subplot(111)

    A = i
    B = j

    for ij in zip(A, B):                                       
        ax.annotate(f'{properties_dictionary}', xy=ij,)
        ax.grid()

    plt.show()  




#print (df)
#print(df.head())

#for col in df.columns:
#   print(col)

#print(df.columns.tolist())

def ranking():
    x=input('x-axis')
    y=input('y-axis')

    max_index=x.index(max(x))
    #print (max_index)
    print ("the best material is")
    print (df.MATERIAL[max_index])
    print("it has a")
    print (x)
    print ("value of")
    print (df.freshwateruse[max_index])
    print("and a")
    print(y)
    print("value of")
    print (df.Carbonfootprint[max_index])
