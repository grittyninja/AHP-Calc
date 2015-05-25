from sys import argv as alt

def kuadratMat(temp):
    le = len(temp)
    i = 0
    matTemp2 = []
    while(i < le):
        matTemp1 = []
        j = 0
        while(j < le):
            it = 0
            vTemp = 0
            while(it < le):
                vTemp += (temp[i][it]*temp[it][j])
                it += 1
            matTemp1.append(vTemp)
            j += 1
        matTemp2.append(matTemp1)
        i += 1
    return matTemp2

def eigenVector(temp):
    matTemp = []
    i = 0
    total = sum(map(sum, temp))
    while(i < len(temp)):
        matTemp.append(sum(temp[i])/total)
        i += 1
    return matTemp

def displayMatrix(temp):
    for i in range(len(temp)):
        line = "\t"
        for j in range(len(temp)):
            line += str("{:.2f}".format(temp[i][j]))
            if(j!=len(temp)-1):
                line += " | "
        print(line)

def displayArray(temp):
    line = "\t\t"
    for i in range(len(temp)):
        line += str("{:.2f}".format(temp[i]))
        if(i!=len(temp)-1):
            line += " | "
    print(line)

def getCR(matr,eigen):
    # CR = CI / RI
    RITable = [0,0,0,0.58,0.90,1.12,1.24,1.32,1.41] # Random Index
    RI = RITable[len(matr)]
    weightedSum = []
    aveWS = []
    for i in range(len(matr)):
        weighted = 0
        for j in range(len(matr)):
            weighted += matr[i][j]*eigen[j]
        weightedSum.append(weighted)
    print("\n\nWeighted Sum Vector : ",end="")
    displayArray(weightedSum)
    for i in range(len(matr)):
        aveWS.append(weightedSum[i]/eigen[i])
    ave = sum(aveWS)/len(aveWS)
    print("Consistency Vector : ",end="")
    displayArray(aveWS)
    print("Average Consistency Vector : ",end="")
    print("\t\t"+str("{:.2f}".format(ave)))
    CI = ((ave - len(matr))/(len(matr)-1))
    print("CI : \t\t"+str("{:.2f}".format(CI)))
    print("RI : \t\t"+str("{:.2f}".format(RI)))
    print("CR : \t\t"+str("{:.2f}".format(CI/RI)))

def ahp(temp,matr):
    i = 1
    loc = matr
    while(i <= temp):
        print("\nIterasi "+str(i)+" :")
        loc = kuadratMat(loc)
        displayMatrix(loc)
        print("\n\tEigen Value :")
        displayArray(eigenVector(loc))
        i += 1
    getCR(matr,eigenVector(loc))


def Main():
    li = list(map(int, alt[1:])) ; matr = []; i = 0
    while(i < len(li)):
        j = 0
        temp = []
        while(j < len(li)):
            temp.append(li[i]/li[j])
            j+=1
        matr.append(temp)
        i+=1
    print("Pairwise Comparison Matrix :\n")
    displayMatrix(matr)
    ahp(2,matr) # do AHP with two iteration

if __name__ == "__main__":
    Main()