solutionlist = []
submissionlist = []
#read solution
fd = open('solution.txt','r') 
for line in fd:
    line = line[12:]
    line = line.rstrip('\n')
    line = line.rstrip()
    solutionlist.append(line.split(' '))
fd.close()
solutionlist = solutionlist [1:]
#read submission
fd = open('submission.txt','r') 
for line in fd:
    d ={}
    line = line[12:]
    line = line.rstrip('\n')
    line = line.rstrip()
    line = line.split(' ')
    for position in range(len(line)):
        d[line[position]] = position 
    submissionlist.append(d)
fd.close()
submissionlist = submissionlist[1:]

# MAP
result = 0
for query in range (len(solutionlist)):
    d = submissionlist[query]
    pos = []
    sum = 0
    i = 0
    for document in range (len(solutionlist[query])):
        pos.append(d.get(solutionlist[query][document]) + 1)
    pos.sort()
    for value in pos :
        i = i + 1
        sum = sum + i / value
    result = result + sum / len(solutionlist[query])#Divide by solution documents number

result = result / len(solutionlist)#Divide by total query number
print(result)
