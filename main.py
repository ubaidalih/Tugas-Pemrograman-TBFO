import CFGtoCNF
import cyk
import sys
import operatorsplit as spl

# def cyk(w):
#     n = len(w)
#     dp = [[set([]) for i in range(n)] for j in range(n)]

#     for i in range(n):
#         for var in cnfGram.items():
#                 for termin in var[1]:
#                     if len(termin) == 1 and termin[0] == w[i]:
#                         dp[i][i].add(var[0])

#     for l in range(2,n+1):
#         for i in range (0,n-l+1):
#             j = i+l-1
#             for k in range (i,j):
#                 for var in cnfGram.items():
#                     for prod in var[1] :
#                         if len(prod) == 2 :
#                             if(prod[0] in dp[i][k]) and (prod[1] in dp[k+1][j]):
#                                 dp[i][j].add(var[0])
#     print(dp)
#     print(dp[0][n-1])
#     if "S0" in dp[0][n-1] :
#         print("true")
#         #return True
#     else :
#         print("false")
#         #return False

K, V, Productions = [],[],[]
variablesJar = ["A1", "B1", "C1", "D1", "E1", "F1", "G1", "H1", "I1", "J1", "K1", "L1", "M1", "N1", "O1", "P1", "Q1", "R1", "S1", "T1", "U1", "V1", "W1", "X1", "Y1", "Z1",
"A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2", "I2", "J2", "K2", "L2", "M2", "N2", "O2", "P2", "Q2", "R2", "S2", "T2", "U2", "V2", "W2", "X2", "Y2", "Z2",
"A3", "B3", "C3", "D3", "E3", "F3", "G3", "H3", "I3", "J3", "K3", "L3", "M3", "N3", "O3", "P3", "Q3", "R3", "S3", "T3", "U3", "V3", "W3", "X3", "Y3", "Z3",
"A4", "B4", "C4", "D4", "E4", "F4", "G4", "H4", "I4", "J4", "K4", "L4", "M4", "N4", "O4", "P4", "Q4", "R4", "S4", "T4", "U4", "V4", "W4", "X4", "Y4", "Z4",
"A5", "B5", "C5", "D5", "E5", "F5", "G5", "H5", "I5", "J5", "K5", "L5", "M5", "N5", "O5", "P5", "Q5", "R5", "S5", "T5", "U5", "V5", "W5", "X5", "Y5", "Z5"]

for nonTerminal in V:
	if nonTerminal in variablesJar:
		variablesJar.remove(nonTerminal)
if len(sys.argv) > 2:
	modelPath = str(sys.argv[2])
else:
	modelPath = 'grammar2.txt'
K, V, Productions = CFGtoCNF.loadModel( modelPath )
Productions = CFGtoCNF.CFGtoCNF(Productions,V,K,variablesJar)
cnfGram = CFGtoCNF.prodToDict(Productions)
open('out2.txt', 'w').write(	CFGtoCNF.displayCNF(Productions) )

filename = sys.argv[1]
print("Compiling...")

output,valid = spl.splitOperator(filename)
if(valid):
	cyk.cyk(output,cnfGram)