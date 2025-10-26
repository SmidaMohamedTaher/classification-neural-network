import  pandas as pd 
from classes.ProcessingData import ProcessingData as mpd
from classes.layers import Layers as ly
import random




df = mpd.getCsvData('bank.csv',';')
df = mpd.hotCoding(df)

layer1 = ly.generateLayer(16,50)
layer2 = ly.generateLayer(2,16)

print(layer1)
print("\n-------------------------\n")
print(layer2)





# print(df.shape[1])
# print(20*"---")
# print(df)