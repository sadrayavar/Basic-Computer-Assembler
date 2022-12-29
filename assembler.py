memRef = ["AND", "ADD", "LDA", "STA", "BUN", "BSA", "ISZ"]
regRef = ["CLA", "CLE", "CMA", "CME", "CIR", "CIL",
          "INC", "SPA", "SNA", "SZA", "SZE", "HLT"]
ioRef = ["INP", "OUT", "SKI", "SKO", "ION", "IOF"]
pseuCode = ["ORG", "END", "DEC", "HEX"]

# file management
inFile = open('sumLoop.asm', 'r')
text = inFile.readlines()
outFile = open('output.txt', 'w')

symbolTable = []


def binTwoComp(decNum):
    binNum = list(bin(int(decNum)))
    if binNum == ['0', 'b', '0']:
        return '0'
    elif binNum[0] == '-':
        # Complement 1 (NOT)
        isNot = ''
        for i in binNum[2:]:
            if i == '0':
                isNot += '1'
            else:
                isNot += '0'

        # Complement 2
        compedNum = bin(int(isNot, 2)+1)[2:]

        # create zero base for output
        output = []
        for i in range(len(binNum[3:])):
            output.append('0')

        # put complemented number on zero base output
        for i in range(len(compedNum)):
            output[-i-1] = compedNum[-i-1]

        # turn output from list to string
        stringedOut = '1'
        for i in output:
            stringedOut += i

        return stringedOut
    else:
        output = '0'
        for i in binNum[2:]:
            output += i

        return output


def firstPass():
    # scan line code types
    lineAddress = 0

    for line in text:

        # check label
        isLabel = True
        for elem in memRef+regRef+ioRef+pseuCode:
            if elem == line[0:3]:
                isLabel = False

        if isLabel:
            symbolTable.append([line[0:3], lineAddress])
            lineAddress += 1
        else:
            if line[0:3] == "ORG":
                lineAddress = int(line[4:])
            else:
                if line[0:3] == "END":
                    secondPass()
                    return
                else:
                    lineAddress += 1


def secondPass():
    # scan line code types
    lineAddress = 0

    # set instruction start
    for line in text:
        instStart = 0
        if len(line) > 3:
            if line[3] == ',':
                instStart = 5

        # check pseudo
        isPseudo = False
        for elem in pseuCode:
            if line[instStart:instStart+3] == elem:
                isPseudo = True

        if isPseudo:
            if line[0:3] == "ORG":
                lineAddress = int(line[4:])
                continue
            else:
                if line[0:3] == "END":
                    print(
                        '####\n## Done\n## You can see the result in the output.txt\n####')
                    return
                else:
                    # convert number to binary
                    if line[instStart:instStart+3] == "DEC":
                        temp = binTwoComp(int(line[4+instStart:]))
                    elif line[instStart:instStart+3] == "HEX":
                        temp = binTwoComp(int(line[4+instStart:], 16))

                    neg = 0
                    if temp[0] == '1':
                        neg = 1
                        zeroBase[0] = '1'

                    zeroBase = []
                    for i in range(16):
                        zeroBase += str(neg)

                    for i in range(len(temp)-neg):
                        zeroBase[-i-1] = temp[-i-1]

                    output = ''
                    for i in range(len(zeroBase)):
                        output += zeroBase[i]

                    outFile.write(str(bin(lineAddress))[2:] + '\t'+output+'\n')
                    lineAddress += 1
        else:
            # Check MRI
            isMRI = False
            for i in memRef:
                if line[instStart:instStart+3] == i:
                    isMRI = True

            if isMRI:
                output = ''
                # set addressing mode
                if line[-2] == 'i' or line[-2] == 'I':
                    output += '1'
                else:
                    output += '0'
                # Get operation code and set bits 12-14
                if line[instStart:instStart+3] == 'AND':
                    output += '000'
                elif line[instStart:instStart+3] == 'ADD':
                    output += '001'
                elif line[instStart:instStart+3] == 'LDA':
                    output += '010'
                elif line[instStart:instStart+3] == 'STA':
                    output += '011'
                elif line[instStart:instStart+3] == 'BUN':
                    output += '100'
                elif line[instStart:instStart+3] == 'BSA':
                    output += '101'
                else:
                    output += '110'
                # Search address-symbol table for binary equivalent of symbol address and set bits 0-11
                for i in symbolTable:
                    if line[instStart+4:instStart+7] == i[0]:
                        temp = ['0', '0', '0', '0', '0', '0',
                                '0', '0', '0', '0', '0', '0']
                        for j in range(len(str(bin(i[1]))[2:])):
                            temp[-j-1] = str(bin(i[1]))[-j-1]
                        for i in temp:
                            output += i
                # assemble all parts of the binary instruction and store in location given by lc
                outFile.write(str(bin(lineAddress))[2:] + '\t'+output+'\n')
                lineAddress += 1
            else:
                # Check valid non MRI
                validNonMRI = False
                for i in regRef+ioRef:
                    if line[instStart:instStart+3] == i:
                        validNonMRI = True
                        break

                if validNonMRI:
                    # store binary equivalent of instruction in location given by lc
                    output = ''
                    if line[instStart:instStart+3] == 'CLA':
                        output += '0111100000000000'
                    elif line[instStart:instStart+3] == 'CLE':
                        output += '0111010000000000'
                    elif line[instStart:instStart+3] == 'CMA':
                        output += '0111001000000000'
                    elif line[instStart:instStart+3] == 'CME':
                        output += '0111000100000000'
                    elif line[instStart:instStart+3] == 'CIR':
                        output += '0111000010000000'
                    elif line[instStart:instStart+3] == 'CIL':
                        output += '0111000001000000'
                    elif line[instStart:instStart+3] == 'INC':
                        output += '0111000000100000'
                    elif line[instStart:instStart+3] == 'SPA':
                        output += '0111000000010000'
                    elif line[instStart:instStart+3] == 'SNA':
                        output += '0111000000001000'
                    elif line[instStart:instStart+3] == 'SZA':
                        output += '0111000000000100'
                    elif line[instStart:instStart+3] == 'SZE':
                        output += '0111000000000010'
                    elif line[instStart:instStart+3] == 'HLT':
                        output += '0111000000000001'
                    elif line[instStart:instStart+3] == 'INP':
                        output += '1111100000000000'
                    elif line[instStart:instStart+3] == 'OUT':
                        output += '1111010000000000'
                    elif line[instStart:instStart+3] == 'SKI':
                        output += '1111001000000000'
                    elif line[instStart:instStart+3] == 'SKO':
                        output += '1111000100000000'
                    elif line[instStart:instStart+3] == 'ION':
                        output += '1111000010000000'
                    elif line[instStart:instStart+3] == 'IOF':
                        output += '1111000001000000'
                    outFile.write(str(bin(lineAddress))[2:] + '\t'+output+'\n')
                    lineAddress += 1
                else:
                    print('Error in line:\t', lineAddress)
                    lineAddress += 1


firstPass()

inFile.close()
outFile.close()
