from classes.ProcessingData import ProcessingData as mpd
from classes.layers import Layers as ly
from classes.cal import Cal as cl

df = mpd.getCsvData('bank.csv',';')
df = mpd.hotCoding(df)

layer1 = ly.generateLayer(16,48)
layer2 = ly.generateLayer(1,16)

out = cl.calAll(df,layer1,layer2)