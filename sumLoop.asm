ORG 0100
LDA ADS
STA PTR
LDA NBR
STA CTR
CLA
LOP, ADD PTR i
ISZ PTR
ISZ CTR
BUN LOP
STA SUM
HLT
ADS, HEX 0150
PTR, HEX 0000
NBR, DEC -100
CTR, HEX 0000
SUM, HEX 0000
ORG 0150
DEC 1
DEC 7
DEC 7
DEC 7
DEC 7
DEC 4
DEC 4
DEC 6
DEC 4
DEC 7
DEC 4
DEC 5
DEC 5
DEC 7
DEC 7
DEC 7
DEC 6
DEC 8
DEC 7
DEC 7
DEC 7
DEC 7
DEC 7
DEC 1
DEC 7
DEC 7
DEC 7
DEC 7
DEC 7
DEC 7
DEC 7
DEC 7
DEC 5
DEC 7
DEC 5
DEC 5
DEC 5
DEC 7
DEC 5
DEC 5
DEC 5
DEC 5
DEC 5
DEC 5
DEC 5
DEC 5
DEC 5
DEC 7
DEC 5
DEC 7
DEC 5
DEC 5
DEC 5
DEC 7
DEC 5
DEC 5
DEC 5
DEC 5
DEC 7
DEC 5
DEC 5
DEC 5
DEC 7
DEC 7
DEC 5
DEC 5
DEC 5
DEC 7
DEC 5
DEC 5
DEC 7
DEC 5
DEC 5
DEC 5
DEC 5
DEC 5
DEC 5
DEC 5
DEC 5
DEC 5
DEC 7
DEC 5
DEC 5
DEC 5
DEC 5
DEC 8
DEC 7
DEC 7
DEC 4
DEC 5
DEC 7
DEC 5
DEC 7
DEC 5
DEC 7
DEC 7
DEC 7
DEC 7
DEC 7
DEC -111
END