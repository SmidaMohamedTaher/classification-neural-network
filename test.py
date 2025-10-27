from classes.ProcessingData import ProcessingData as mpd
from classes.layers import Layers as ly

def calculOutput1( df , num , layer1 ):
    list = df.drop(columns=['y']).iloc[num].tolist()
    output = []
    one = []
    for j in range(16):
        for i in range(48):
            one.append(list[i] * layer1[j][i])
        output.append(sum(one))
        one.clear()
    return output 

df = mpd.getCsvData('bank.csv',';')
df = mpd.hotCoding(df)

layer1 = ly.generateLayer(16,48)
layer2 = ly.generateLayer(2,16)

print(len(calculOutput1(df,48,layer1)))

