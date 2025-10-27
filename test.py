from classes.ProcessingData import ProcessingData as mpd
from classes.layers import Layers as ly
import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# def calculOutput1( df , num , layer1 ):
#     list = df.drop(columns=['y']).iloc[num].tolist()
#     output = []
#     one = []
#     for j in range(16):
#         for i in range(48):
#             one.append(list[i] * layer1[j][i])
#         output.append(sum(one))
#         one.clear()
#     return output 

def calculOutput1(df, num, layer1):
    
    row = df.drop(columns=['y']).iloc[num].to_numpy()  
    layer1 = np.array(layer1)  
    
    
    output = np.dot(layer1, row)  
    
    return output.tolist()

def calculOutput2(list , layer2):
    output = []
    one = []
    for j in range(1):
        for i in range(16):
            one.append(list[i] * layer2[j][i])
        output.append(sum(one))
        one.clear()
    if len(output) == 1:
        y = sigmoid(output[0])
        return 1 if y >= 0.5 else 0
    return output 

def calAll(df,layer1,layer2):
    num = df.shape[0]
    out = []
    list = []
    for i in range(num):
        list = calculOutput1(df,i,layer1)
        out.append(calculOutput2(list,layer2))
    return out 


df = mpd.getCsvData('bank.csv',';')
df = mpd.hotCoding(df)

layer1 = ly.generateLayer(16,48)
layer2 = ly.generateLayer(1,16)


print(calAll(df,layer1,layer2))
