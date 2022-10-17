# Algorithms 3
V_rest = -75
V_threshold = -65
spike = 0
V_membrane = V_rest
inputCurrent = 1 #constant for all synapses
synapticWeights = [0.01, 0.8, 1.2, 2.3]
t = 1

while t<= 5:
    spikeList=[]
    totalInput = 0
    for i in synapticWeights:
        totalInput = totalInput+i*inputCurrent
    V_membrane = V_membrane + totalInput
    
    if V_membrane >= V_threshold:
        spike = 1
        spikeList.append(spike)
        V_membrane = V_rest
    else:
        spike = 0
        spikeList.append(spike)
    t = t+1
    
    print(spikeList)


