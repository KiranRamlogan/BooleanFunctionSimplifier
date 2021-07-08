import BooleanFunctionSimplifier as BFS
import GetCoreMinterms as GCM

#Uses information from the GUI to get the minterms dictionary 'coreMinterms' and simplify the boolean function
def runModel(variableNames, minterms):
    error = False
    coreMinterms = GCM.GetCoreMinterms(len(variableNames))
    for i in range(0,len(minterms)):
        if(minterms[i] not in coreMinterms):
            error = True
    if(error == False):
        simplifiedExpression = BFS.runProgram(coreMinterms, len(variableNames), variableNames, minterms)
        return simplifiedExpression
    else:
        return ''

