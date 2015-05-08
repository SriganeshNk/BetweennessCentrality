def normalizeOut(filename,index):
    f = open(filename,'r')
    x = 0
    BC = []
    for line in f:
        if line[0] == '<':
            x += 1
            continue
        if line[0] == 'B':
            break
        if len(line.strip()) > 0 and x == 1:
            line = line.strip().split(' ')
            BC.append(float(line[0]))
    f.close()
    print BC[index]/sum(BC)

normalizeOut('7_Directed_Out.txt',2)
