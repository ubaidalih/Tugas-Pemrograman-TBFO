import re

def splitOperator(filename):
    f = open(filename, "r")
    input = f.read()
    f.close()

    input = input.split()
    output = input

    operator = ['=', '!=', '==', '>=', '<=', '<', '>', ':', ',', '/', '-', r'\+', r'\*', r'\*\*', r'\'', r'\"', r'\'\'\'', r'\(', r'\)']
    
    for oper in operator:
        temp = []    
        for statement in output:
            splitting = r'[A..z]*(' + oper + r')[A..z]*'
            elmt = re.split(splitting, statement)
            
            for splitted in elmt:
                temp.append(splitted) 
        output = temp

    temp = []
    for statement in output:
        checkStrip = statement.split()
        for splitted in checkStrip: 
            temp.append(splitted)

    output = temp
    output = [string for string in output]
    print(output)

splitOperator("tes.txt")