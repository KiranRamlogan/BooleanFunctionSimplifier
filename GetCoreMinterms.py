#Copies and Adjusts the numbers in the "Minterms" file to work in the simplifier
def GetCoreMinterms(numVariables):
    coreMinterms = {'m0':[0]}
    numMinterms = pow(2, numVariables)  #The number of minterms needed is = 2^n

    with open("BinaryNumbers.txt", 'r', encoding = 'utf-8') as f:
        for i in range(1,numMinterms):
            line = f.readline()
            line = list(line.strip('\n'))
            for x in range(0, len(line)):
                line[x] = int(line[x])
            key = 'm' + str(i)
            coreMinterms[key] = line

    for i in range(0,len(coreMinterms)):    #Fills in empty spaces with zeros
        key = 'm' + str(i)
        if(len(coreMinterms[key]) != numVariables):
            diff = numVariables - len(coreMinterms[key])
            for x in range(0,diff):
                coreMinterms[key].insert(0,0)
    return coreMinterms


